import pandas as pd


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


def parse_data_set(filepath, index_files, n):
    for nbr in index_files:
        datapath = filepath + nbr
        df = pd.read_csv(datapath+".csv", sep=',', dtype=object)

        # convert columns to float type if possible
        for key in df.keys():
            df[key] = df[key].astype('float', errors='ignore')

        f = open(datapath+"_result.txt", "w+")

        # max and mean per execution
        # -------------------------------
        df_exec = pd.DataFrame(columns=df.keys())
        df_max_exec = pd.DataFrame(columns=df.keys())
        df_final = pd.DataFrame(columns=df.keys())
        size = 0
        for index, row in df.iterrows():
            df_exec = df_exec.append(row, ignore_index=True)
            if (index % n) == 2:
                max_row = df_exec.max()
                df_max_exec = df_max_exec.append(max_row, ignore_index=True)
                df_exec.drop(df_exec.index, inplace=True)
                size += 1

        row_sum = df_max_exec.sum()

        for items in row_sum.iteritems():
            if type(items[1]) == float:
                row_sum[items[0]] = row_sum[items[0]] / size

        df_final = df_final.append(row_sum, ignore_index=True)
        format_data_and_store_in_file_max(df_final, f)
        # -------------------------------

        # mean between the each node
        # -------------------------------
        # gb = df.groupby(['node_name'])
        # size = gb.size()[0]
        # df_aggr = gb.sum()

        # df_final = df_aggr.div(size)
        # util.format_data_and_store_in_file_3_nodes(df_final, f)
        # -------------------------------

        f.close()

