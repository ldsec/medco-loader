
def format_data_and_store_in_file_3_nodes(df, f):
    for key in df.keys():
        key_format = "{0:50}"

        val_format = ""
        for i in range(1, len(df[key])+1):
            val_format = val_format + " {" + str(i) + "}"

        line = key_format + val_format
        f.write(line.format(key+":", df[key][0], df[key][1], df[key][2])+"\n")


def format_data_and_store_in_file_max(df, f):
    for key in df.keys():
        line = "{0:50} {1}"
        f.write(line.format(key+":", df[key][0])+"\n")