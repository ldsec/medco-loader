import pandas as pd

folder = "patient_list"
datapath = folder + "/" + "output_queries_format.csv"
df = pd.read_csv(datapath, sep=',', dtype=object)

output = open("result.txt", "w+")

for key in df.keys():
    keyFormat = "{0:50}"

    valFormat = ""
    i = 1
    for el in df[key]:
        valFormat = valFormat + " {" + str(i) + "}"
        i += 1

    line = keyFormat + valFormat
    output.write(line.format(key+":", df[key][0], df[key][1], df[key][2])+"\n")

output.close()
