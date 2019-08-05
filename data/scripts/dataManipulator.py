import pandas as pd
import numpy as np


# PLEASE USE THIS TO CONFIGURE YOUR SCRIPT #
# ---------------------------------------- #
# specify input data files
cli_in_fn = "../genomic/tcga_cbio/clinical_data.csv"
mut_in_fn = "../genomic/tcga_cbio/mutation_data.csv"
# specify output folder
out_folder = "../genomic/tcga_cbio/manipulations/"
# ---------------------------------------- #

df_cli = pd.read_csv(cli_in_fn, sep='\t', dtype=object)
df_mut = pd.read_csv(mut_in_fn, sep='\t', dtype=object)

def save(df_cli_new, df_mut_new):
    while True:
        opt = input("\nDo you wish to save data (y|n):")

        if opt not in ["y", "n"]:
            print("Wrong option!")
            continue

        if opt == "y":
            filename = input("Specify filename:")
            df_cli_new.to_csv(out_folder + filename+"_clinical_data.csv", sep='\t', encoding='utf-8', index=False)
            df_mut_new.to_csv(out_folder + filename+"_mutation_data.csv", sep='\t', encoding='utf-8', index=False)
            return

        if opt == "n":
            return


def replace_ids(df, column, it):
    str_append = '0'
    for i in range(0, it):
        str_append = str_append + '0'
    df[column] = df[column] + str_append
    return df


def new_ids(df_cli_new, df_mut_new, it):
    # change new data with new patient ids
    df_cli_new = replace_ids(df_cli_new, "PATIENT_ID", it)
    df_mut_new = replace_ids(df_mut_new, "PATIENT_ID", it)

    # change new data with new patient ids
    df_cli_new = replace_ids(df_cli_new, "SAMPLE_ID", it)
    df_mut_new = replace_ids(df_mut_new, "SAMPLE_ID", it)

    return df_cli_new, df_mut_new


def random_replication():
    while True:
        num_str = input("\nNumber of patients for the new dataset:")

        try:
            num = int(num_str)
        except ValueError:
            print("That's not an int!")
            continue

        total_patients = df_cli["PATIENT_ID"].unique()
        nbr_total_patients = len(total_patients)
        if nbr_total_patients >= num:
            print("Replication means that: new number of patients > old number of patients")
            continue

        df_cli_cpy = df_cli.copy(True)
        df_mut_cpy = df_mut.copy(True)

        remaining_patients = num - nbr_total_patients
        it = 0
        while remaining_patients != 0:
            if remaining_patients >= nbr_total_patients:
                df_cli_new = df_cli.copy(True)
                df_mut_new = df_mut.copy(True)

                # change new data with new ids
                df_cli_new, df_mut_new = new_ids(df_cli_new, df_mut_new, it)

                # concatenate data
                df_cli_cpy = pd.concat([df_cli_cpy, df_cli_new])
                df_mut_cpy = pd.concat([df_mut_cpy, df_mut_new])

                remaining_patients = remaining_patients - nbr_total_patients
            else:
                list_patients = np.random.choice(total_patients, remaining_patients, replace=False)

                df_cli_new = df_cli.loc[df_cli["PATIENT_ID"].isin(list_patients)]
                df_mut_new = df_mut.loc[df_mut["PATIENT_ID"].isin(list_patients)]

                # change new data with new ids
                df_cli_new, df_mut_new = new_ids(df_cli_new, df_mut_new, it)

                # concatenate data
                df_cli_cpy = pd.concat([df_cli_cpy, df_cli_new])
                df_mut_cpy = pd.concat([df_mut_cpy, df_mut_new])

                remaining_patients = 0
            print("Remaining patients:", remaining_patients)
            it = it + 1
        save(df_cli_cpy, df_mut_cpy)
        return


def random():
    while True:
        num_str = input("\nNumber of patients for the new dataset:")

        try:
            num = int(num_str)
        except ValueError:
            print("That's not an int!")
            continue

        total_patients = df_cli["PATIENT_ID"].unique()
        list_patients = np.random.choice(total_patients, num, replace=False)

        df_cli_new = df_cli.loc[df_cli["PATIENT_ID"].isin(list_patients)]
        df_mut_new = df_mut.loc[df_mut["PATIENT_ID"].isin(list_patients)]

        save(df_cli_new, df_mut_new)
        return


def specific():
    while True:
        path = input("\nPlease introduce the the path to a file with a list of PATIENT_IDs to be selected from the "
                         "original dataset.")

        try:
            df = pd.read_csv(path, sep='\t', dtype=object, header=None)
        except IOError:
            print('File not found')
            continue

        list_patients = np.array(df[0])

        df_cli_new = df_cli.loc[df_cli["PATIENT_ID"].isin(list_patients)]
        df_mut_new = df_mut.loc[df_mut["PATIENT_ID"].isin(list_patients)]

        save(df_cli_new, df_mut_new)
        return


def menu():
    while True:
        print("\n#--- MENU ---#")
        print("(1) Random Replication")
        print("(2) Random")
        print("(3) Specific")
        print("(4) Help")
        print("(5) Exit")

        opt = input("Option:")

        if opt not in ["1", "2", "3", "4", "5"]:
            print("Wrong option!")
            continue

        # randomly replicates the dataset (and respective mutations)
        if opt == "1":
            random_replication()

        # randomly filters the patients (and respective mutations)
        if opt == "2":
            random()

        # specific filters the patients (and respective mutations) based on a file wit patient IDs
        if opt == "3":
            specific()

        # some help noob
        if opt == "4":
            print("HELP\n")
            print("--------------------------------------------------------------------------------------------------")
            print("This is a small application to manipulate the tcga_cbio data.\n\nBEFORE ANYTHING! Check if you "
                  "have configured the script (check the top lines on how to do it)."
                  "\n\nWe have two modes to manipulate "
                  "the data: \n- (Random replication) where we replicate the number of patients (multiple copies)"
                  "\n- (Random) where we sample a random number of patients to build a new smaller dataset;"
                  "\n- (Specific) where we specify (through a file) the patients' IDs we want to include."
                  "\n\nNow go an play...")
            print("--------------------------------------------------------------------------------------------------")

        # well is an exit what do you expect
        if opt == "5":
            return


menu()
