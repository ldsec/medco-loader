import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'Bitstream Vera Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [7, 52, 150, 451, 585, 940, 1366, 1511],
    'insecure_i2b2': [1180.8+121.8, 2493.2+115.0, 5019.2+159.3, 13332.4+586.2, 13639.8+197.4,
                      20842.5+257.9, 28605.4+344.2, 31764.3+373.4],
    'medco':  [1361.8, 2810.2, 5583.8, 14603.1, 14692.7, 22310.6, 30553.3, 33850.3],
}

# convert to seconds
raw_data['insecure_i2b2'] = [x / 1000 for x in raw_data['insecure_i2b2']]
raw_data['medco'] = [x / 1000 for x in raw_data['medco']]

df = pd.DataFrame(raw_data, raw_data['x_label'])

fig, ax = plt.subplots(1, figsize=(17, 11))
ax.plot(raw_data['x_label'], raw_data['medco'],
        label='MedCo', linewidth=2, ls='--',
        marker='o', markersize=7)
ax.plot(raw_data['x_label'], raw_data['insecure_i2b2'],
        label='Insecure i2b2', linewidth=2,
        marker='o', markersize=7)

ax.set_ylim([0, 40])
ax.set_xlim([0, 1600])

plt.setp(ax.get_yticklabels()[0], visible=False)

# # Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Size of the result set", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('patient_list.pdf', format='pdf')
