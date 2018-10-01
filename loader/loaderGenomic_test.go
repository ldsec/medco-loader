package loader_test

import (
	"encoding/base64"
	"github.com/dedis/onet"
	"github.com/dedis/onet/app"
	"github.com/dedis/onet/log"
	"github.com/lca1/medco-loader/loader"
	"github.com/lca1/unlynx/lib"
	"github.com/stretchr/testify/assert"
	"os"
	"testing"
)

const (
	clinicalOntology = "../data/genomic/tcga_cbio/manipulations/80_node0_clinical_data.csv"
	genomicOntology  = "../data/genomic/tcga_cbio/manipulations/80_node0_mutation_data.csv"
	clinicalFile     = "../data/genomic/tcga_cbio/manipulations/80_node0_clinical_data.csv"
	genomicFile      = "../data/genomic/tcga_cbio/manipulations/80_node0_mutation_data.csv"

	//clinicalOntology = "../data/genomic/tcga_cbio/clinical_data.csv"
	//genomicOntology  = "../data/genomic/tcga_cbio/mutation_data.csv"
	//clinicalFile     = "../data/genomic/tcga_cbio/clinical_data.csv"
	//genomicFile      = "../data/genomic/tcga_cbio/mutation_data.csv"
)

func getRoster(groupFilePath string) (*onet.Roster, *onet.LocalTest, error) {
	// empty string: make localtest
	if len(groupFilePath) == 0 {
		log.Info("Creating local test roster")

		local := onet.NewLocalTest(libunlynx.SuiTe)
		_, el, _ := local.GenTree(3, true)
		return el, local, nil

		// generate el with group file
	} else {
		log.Info("Creating roster from group file path")

		f, err := os.Open(groupFilePath)
		if err != nil {
			log.Error("Error while opening group file", err)
			return nil, nil, err
		}
		el, err := app.ReadGroupDescToml(f)
		if err != nil {
			log.Error("Error while reading group file", err)
			return nil, nil, err
		}
		if len(el.Roster.List) <= 0 {
			log.Error("Empty or invalid group file", err)
			return nil, nil, err
		}

		return el.Roster, nil, nil
	}
}

func generateFiles(t *testing.T, el *onet.Roster, entryPointIdx int) {
	log.SetDebugVisible(1)

	fOntologyClinical, err := os.Open(clinicalOntology)
	assert.True(t, err == nil, err)
	fOntologyGenomic, err := os.Open(genomicOntology)
	assert.True(t, err == nil, err)

	fClinical, err := os.Open(clinicalFile)
	assert.True(t, err == nil, err)
	fGenomic, err := os.Open(genomicFile)
	assert.True(t, err == nil, err)

	// init global variables
	loader.FileHandlers = make([]*os.File, 0)
	loader.Testing = true
	loader.OntValues = make(map[loader.ConceptPath]loader.ConceptID)
	loader.TextSearchIndex = int64(1)

	for _, f := range loader.FilePathsOntology {
		fp, err := os.Create(f)
		assert.True(t, err == nil, err)
		loader.FileHandlers = append(loader.FileHandlers, fp)
	}

	for _, f := range loader.FilePathsData {
		fp, err := os.Create(f)
		assert.True(t, err == nil, err)
		loader.FileHandlers = append(loader.FileHandlers, fp)
	}

	mapSensitive := make(map[string]struct{}, 11) // DO NOT FORGET!! to modify the '11' value depending on the number of sensitive attributes
	mapSensitive["AJCC_PATHOLOGIC_TUMOR_STAGE"] = struct{}{}
	mapSensitive["CANCER_TYPE"] = struct{}{}
	mapSensitive["CANCER_TYPE_DETAILED"] = struct{}{}
	mapSensitive["HISTOLOGICAL_DIAGNOSIS"] = struct{}{}
	mapSensitive["ICD_O_3_HISTOLOGY"] = struct{}{}
	mapSensitive["ICD_O_3_SITE"] = struct{}{}
	mapSensitive["SAMPLE_TYPE"] = struct{}{}
	mapSensitive["TISSUE_SOURCE_SITE"] = struct{}{}
	mapSensitive["TUMOR_TISSUE_SITE"] = struct{}{}
	mapSensitive["VITAL_STATUS"] = struct{}{}
	mapSensitive["CLIN_M_STAGE"] = struct{}{}

	err = loader.GenerateOntologyFiles(el, entryPointIdx, fOntologyClinical, fOntologyGenomic, mapSensitive)
	assert.True(t, err == nil, err)

	err = loader.GenerateDataFiles(el, fClinical, fGenomic)
	assert.True(t, err == nil, err)

	for _, f := range loader.FileHandlers {
		f.Close()
	}

	fClinical.Close()
	fGenomic.Close()

	fOntologyClinical.Close()
	fOntologyGenomic.Close()
}

func TestSanitizeHeader(t *testing.T) {
	ex := "AJCC_PATHOLOGIC_TUMOR_STAGE"
	res := loader.SanitizeHeader(ex)
	assert.Equal(t, "Ajcc Pathologic Tumor Stage", res)

	ex = "CANCER_TYPE"
	res = loader.SanitizeHeader(ex)
	assert.Equal(t, "Cancer Type", res)

	ex = "CANCER_TYPE_DETAILED"
	res = loader.SanitizeHeader(ex)
	assert.Equal(t, "Cancer Type Detailed", res)
}

func TestGenerateFilesLocalTest(t *testing.T) {
	t.Skip()
	el, local, err := getRoster("")
	assert.True(t, err == nil, err)
	generateFiles(t, el, 0)
	local.CloseAll()
}

func TestGeneratePubKey(t *testing.T) {
	t.Skip()
	el, _, err := getRoster("../data/genomic/group.toml")
	assert.True(t, err == nil, err)

	b, err := el.Aggregate.MarshalBinary()
	assert.True(t, err == nil, err)

	log.LLvl1("Aggregate Key:", base64.StdEncoding.EncodeToString(b))
}

func TestGenerateFilesGroupFile(t *testing.T) {
	t.Skip()
	// todo: fix hardcoded path
	// increase maximum in onet.tcp.go to allow for big packets (for now is the max value for uint32)
	el, _, err := getRoster("/Users/jagomes/Documents/EPFL/MedCo/medco-deployment/configuration-profiles/dev-3nodes-samehost/group.toml")

	assert.True(t, err == nil, err)
	generateFiles(t, el, 0)
}

func TestReplayDataset(t *testing.T) {
	t.Skip()
	err := loader.ReplayDataset(genomicFile, 2)
	assert.True(t, err == nil)
}

func TestGenerateLoadingScript(t *testing.T) {
	t.Skip()
	err := loader.GenerateLoadingDataScript(loader.DBSettings{DBhost: "localhost", DBport: 5434, DBname: "medcodeployment", DBuser: "postgres", DBpassword: "prigen2017"})
	assert.True(t, err == nil)
}

func TestLoadDataFiles(t *testing.T) {
	t.Skip()
	err := loader.LoadDataFiles()
	assert.True(t, err == nil)
}