import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'Bitstream Vera Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [7.11, 9.51, 14.25, 28.2],
    'insecure_i2b2': [73440.85+385.15, 98020.15+388.8, 151112.55+68.45, 312083.8+375.5],
    'medco':  [75592.25, 100206.1, 153244.2, 314200.2],
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

# # Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Size of the data set (Billion rows)", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('data_size.png', format='png')
