import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

raw_data_query = {
    'x_label':  ['1000', '2000', '4000', '8000'],
    'i2b2/shrine': [7.2, 9.2, 12.9, 20.5],                                                          # I2B2/SHRINE
    'medco': [8.4, 9.9, 13.6, 21.9],                                                                # Medco
    'medco+': [190.7, 9.9+172.4+21, 13.6+172.4+42.1, 21.9+172.4+87.3],                 # Medco+
}

font = {'family': 'Bitstream Vera Sans',
        'size': 24}

plt.rc('font', **font)

df = pd.DataFrame(raw_data_query, raw_data_query['x_label'])

N = 4
ind = np.arange(N)  # The x locations for the groups

# Create the general blog and the "subplots" i.e. the bars
fig, ax1 = plt.subplots(1, figsize=(14, 12))

# Set the bar width
bar_width = 0.3


ax1.bar(ind, df['i2b2/shrine'], width=bar_width, label='i2b2/SHRINE', alpha=0.5, color='#1abc78', edgecolor='black')
ax1.bar(ind + bar_width, df['medco'], width=bar_width, label='MedCo', alpha=0.5, color='#3232FF', edgecolor='black')
ax1.bar(ind + bar_width + bar_width, df['medco+'], width=bar_width, label='MedCo+', alpha=0.5,
        color='#bc1a1a', edgecolor='black')

# Set the x ticks with names
ax1.set_xticks(ind + bar_width)
ax1.set_xticklabels(df['x_label'])
ax1.set_yscale('symlog', basey=10)
ax1.set_ylim([0, 10000])
ax1.set_xlim([-bar_width, ind[0] + 12*bar_width + bar_width])

# Labelling
ax1.text(ind[0] - 0.12, df['i2b2/shrine'][0] + 1,
         str(df['i2b2/shrine'][0]), color='black', fontweight='bold')
ax1.text(ind[1] - 0.12, df['i2b2/shrine'][1] + 1,
         str(df['i2b2/shrine'][1]), color='black', fontweight='bold')
ax1.text(ind[2] - 0.17, df['i2b2/shrine'][2] + 1,
         str(df['i2b2/shrine'][2]), color='black', fontweight='bold')
ax1.text(ind[3] - 0.17, df['i2b2/shrine'][3] + 2,
         str(df['i2b2/shrine'][3]), color='black', fontweight='bold')

ax1.text(ind[0] + bar_width - 0.11, df['medco'][0] + 1,
         str(df['medco'][0]), color='black', fontweight='bold')
ax1.text(ind[1] + bar_width - 0.11, df['medco'][1] + 1,
         str(df['medco'][1]), color='black', fontweight='bold')
ax1.text(ind[2] + bar_width - 0.19, df['medco'][2] + 8,
         str(df['medco'][2]), color='black', fontweight='bold')
ax1.text(ind[3] + bar_width - 0.19, df['medco'][3] + 12,
         str(df['medco'][3]), color='black', fontweight='bold')

ax1.text(ind[0] + bar_width + bar_width - 0.20, df['medco+'][0]+30,
         str(df['medco+'][0]), color='black', fontweight='bold')
ax1.text(ind[1] + bar_width + bar_width - 0.20, df['medco+'][1]+30,
         str(df['medco+'][1]), color='black', fontweight='bold')
ax1.text(ind[2] + bar_width + bar_width - 0.20, df['medco+'][2]+30,
         str(df['medco+'][2]), color='black', fontweight='bold')
ax1.text(ind[3] + bar_width + bar_width - 0.20, df['medco+'][3]+30,
         str(df['medco+'][3]), color='black', fontweight='bold')

# Set the label and legends
ax1.set_ylabel("Runtime (s)", fontsize=32)
ax1.set_xlabel("#patients per site", fontsize=32)
plt.legend(loc='upper left', fontsize=24)

ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)

plt.savefig('./scalability_patients_queryA.pdf', format='pdf')
