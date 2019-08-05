import util

sufix = ['20r_10q_1511p_3n_2.37B', '20r_10q_1511p_3n_3.17B', '20r_10q_1511p_3n_4.75B', '10r_10q_1511p_3n_9.5B']
filepath = "ds+nn/exp_"

util.parse_data_set(filepath, sufix, 3)

sufix = ['6n_2.37B', '6n_3.17B', '6n_4.75B', '6n_9.2B']
filepath = "ds+nn/exp_20r_10q_1511p_"

util.parse_data_set(filepath, sufix, 6)

sufix = ['9n_2.37B', '9n_3.17B', '9n_4.75B', '9n_9.2B']

util.parse_data_set(filepath, sufix, 9)

sufix = ['12n_2.37B', '12n_3.17B', '12n_4.75B', '12n_9.2B']

util.parse_data_set(filepath, sufix, 12)
