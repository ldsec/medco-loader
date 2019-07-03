import pandas as pd

numberPatients = "7"
datapath = "exp_resulting_patients_" + numberPatients
df = pd.read_csv("exp_resulting_patients_52.csv", sep=',', dtype=object)
output = open(datapath+"_result.txt", "w+")

for key in df.keys():
    print(key)


    #keyFormat = "{0:50}"

    #valFormat = ""
    #i = 1
    #for el in df[key]:
    #    valFormat = valFormat + " {" + str(i) + "}"
    #    i += 1

    #line = keyFormat + valFormat
    #output.write(line.format(key+":", df[key][0], df[key][1], df[key][2])+"\n")

output.close()
