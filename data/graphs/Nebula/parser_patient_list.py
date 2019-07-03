import pandas as pd
import util

N = 3
numberPatients = ['7', '52', '150', '451', '585', '940', '1366', '1511']

for nbr in numberPatients:
    datapath = "patient_list/exp_resulting_patients_" + nbr
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
        if (index % N) == 2:
            max_row = df_exec.max()
            df_max_exec = df_max_exec.append(max_row, ignore_index=True)
            df_exec.drop(df_exec.index, inplace=True)
            size+=1

    print(df_max_exec['medco-connector-i2b2-PSM'])
    row_sum = df_max_exec.sum()
    print(row_sum['medco-connector-i2b2-PSM'])

    for items in row_sum.iteritems():
        if type(items[1]) == float:
            row_sum[items[0]] = row_sum[items[0]] / size

    df_final = df_final.append(row_sum, ignore_index=True)
    util.format_data_and_store_in_file_max(df_final, f)
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
