import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

raw_data = {
    'x_label':  ['5', '10', '100', '500'],
    'medco': [0.095, 0.1, 0.26, 0.956],                  # medco
    'medco+': [387+0.1, 387+0.2, 387+0.3, 387+1],        # medco+
}

font = {'family': 'Bitstream Vera Sans',
        'size': 26}

plt.rc('font', **font)

df = pd.DataFrame(raw_data, raw_data['x_label'])

N = 4
ind = np.arange(N)  # The x locations for the groups

fig, ax1 = plt.subplots(1, figsize=(14, 12))

# Set the bar width
bar_width = 0.4

ax1.bar(ind, df['medco'], width=bar_width, label='MedCo', alpha=0.5, color='#3232FF')
ax1.bar(ind + bar_width, df['medco+'], width=bar_width, label='MedCo+', alpha=0.5, color='#bc1a1a')

# Set the x ticks with names
ax1.set_xticks(ind + bar_width/2)
ax1.set_xticklabels(df['x_label'])
ax1.set_ylim([0, 10000])
ax1.set_yscale('symlog', basey=10)
ax1.set_xlim([-bar_width, ind[3] + bar_width + bar_width + bar_width/2])

# Labelling
ax1.text(ind[0] - 0.27, df['medco'][0]+0.05,
         str(df['medco'][0]), color='black', fontweight='bold')
ax1.text(ind[1] - 0.12, df['medco'][1]+0.05,
         str(df['medco'][1]), color='black', fontweight='bold')
ax1.text(ind[2] - 0.19, df['medco'][2]+0.05,
         str(df['medco'][2]), color='black', fontweight='bold')
ax1.text(ind[3] - 0.27, df['medco'][3]+0.1,
         str(df['medco'][3]), color='black', fontweight='bold')

ax1.text(ind[0] + bar_width - 0.22, df['medco+'][0]+30,
         str(df['medco+'][0]), color='black', fontweight='bold')
ax1.text(ind[1] + bar_width - 0.22, df['medco+'][1]+30,
         str(df['medco+'][1]), color='black', fontweight='bold')
ax1.text(ind[2] + bar_width - 0.22, df['medco+'][2]+30,
         str(df['medco+'][2]), color='black', fontweight='bold')
ax1.text(ind[3] + bar_width - 0.15, df['medco+'][3]+30,
         str(int(df['medco+'][3])), color='black', fontweight='bold')

# Set the label and legends
ax1.set_ylabel("Overhead of network traffic (MB)", fontsize=32)
ax1.set_xlabel("#of query concepts", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)

plt.savefig('./network_traffic.pdf', format='pdf')
