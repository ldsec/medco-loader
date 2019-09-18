import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

raw_data_query = {
    'x_label':  ['3', '6', '9', '10'],
    'query_tagging': [0.189, 0.253, 0.315, 0.351],                # Query tagging
    'shuffling_key_switching': [0.008, 0.016, 0.027, 0.033],      # Shuffling + Key Switching
    'total': [0.2, 0.27, 0.34, 0.38],                             # Total
}

font = {'family': 'Bitstream Vera Sans',
        'size': 22}

plt.rc('font', **font)

df = pd.DataFrame(raw_data_query, raw_data_query['x_label'])

N = 4
ind = np.arange(N)  # The x locations for the groups

# Create the general blog and the "subplots" i.e. the bars
fig, ax1 = plt.subplots(1, figsize=(18, 12))

# Set the bar width
bar_width = 0.5

ax1.bar(ind, df['query_tagging'], width=bar_width, label='Query deterministic re-encryption', alpha=0.5,
        color='#f2d70e', edgecolor='black')
ax1.bar(ind, df['shuffling_key_switching'], bottom=df['query_tagging'], width=bar_width,
        label='Results shuffling & re-encryption', alpha=0.5, color='#d1101d', edgecolor='black')

# Set the x ticks with names
ax1.set_xticks(ind)
ax1.set_xticklabels(df['x_label'])
ax1.set_ylim([0, 0.8])
ax1.set_xlim([-bar_width, ind[2] + bar_width + bar_width + bar_width])


# Labelling
ax1.text(ind[0] - 0.08, df['total'][0]+0.01,
         str(df['total'][0]), color='black', fontweight='bold')
ax1.text(ind[1] - 0.11, df['total'][1]+0.01,
         str(df['total'][1]), color='black', fontweight='bold')
ax1.text(ind[2] - 0.11, df['total'][2]+0.01,
         str(df['total'][2]), color='black', fontweight='bold')
ax1.text(ind[3] - 0.11, df['total'][3]+0.01,
         str(df['total'][3]), color='black', fontweight='bold')

# Set the label and legends
ax1.set_ylabel("Overhead of distributed computations (s)", fontsize=22)
ax1.set_xlabel("#of SPUs", fontsize=22)
plt.legend(loc='upper left')

ax1.tick_params(axis='x', labelsize=22)
ax1.tick_params(axis='y', labelsize=22)

plt.savefig('scalability_#servers_queryA.pdf', format='pdf')
