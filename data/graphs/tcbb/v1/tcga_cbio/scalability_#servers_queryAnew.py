import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

raw_data_query = {
    'x_label':  ['3', '6', '9', '10'],
    'empty': [0, 0, 0, 0],
    'query_tagging_A': [0.189, 0.253, 0.315, 0.351],                # Query tagging (Query A)
    'shuffling_key_switching_A': [0.008, 0.016, 0.027, 0.033],      # Shuffling + Key Switching (Query A)
    'total_A': [0.2, 0.27, 0.34, 0.38],                             # Total (A)
    'query_tagging_B': [0.304, 0.414, 0.566, 0.603],                # Query tagging (Query B)
    'shuffling_key_switching_B': [0.006, 0.015, 0.027, 0.03],       # Shuffling + Key Switching (Query B)
    'total_B': [0.31, 0.43, 0.58, 0.63]                             # Total (B)
}

font = {'family': 'Bitstream Vera Sans',
        'size': 24}

plt.rc('font', **font)

df = pd.DataFrame(raw_data_query, raw_data_query['x_label'])

N = 4
ind = np.arange(N)  # The x locations for the groups

# Create the general blog and the "subplots" i.e. the bars
fig, ax1 = plt.subplots(1, figsize=(14, 9))

# Set the bar width
bar_width = 0.3

ax1.bar(ind, df['empty'], width=bar_width, label='Query deterministic re-encryption', alpha=0.5,
        color='white', edgecolor='black', hatch="//")
ax1.bar(ind, df['empty'], width=bar_width, label='Results shuffling & re-encryption', alpha=0.5,
        color='white', edgecolor='black')

ax1.bar(ind, df['query_tagging_A'], width=bar_width, alpha=0.5,
        color='#f2d70e', edgecolor='black', hatch="//")
ax1.bar(ind, df['shuffling_key_switching_A'], bottom=df['query_tagging_A'], width=bar_width,
        alpha=0.5, color='#f2d70e', edgecolor='black')

# Set the x ticks with names
ax1.set_xticks(ind  )
ax1.set_xticklabels(df['x_label'])
ax1.set_ylim([0, 0.6])
ax1.set_xlim([-bar_width, ind[3] + 2*bar_width])


# Labelling
ax1.text(ind[0] - 0.12, df['total_A'][0]+0.005,
         str(df['total_A'][0]), color='black', fontweight='bold')
ax1.text(ind[1] - 0.15, df['total_A'][1]+0.01,
         str(df['total_A'][1]), color='black', fontweight='bold')
ax1.text(ind[2] - 0.15, df['total_A'][2]+0.01,
         str(df['total_A'][2]), color='black', fontweight='bold')
ax1.text(ind[3] - 0.15, df['total_A'][3]+0.01,
         str(df['total_A'][3]), color='black', fontweight='bold')


# Set the label and legends
ax1.set_ylabel("Runtime Overhead (s)", fontsize=32)
ax1.set_xlabel("#of SPUs", fontsize=32)
plt.legend(loc='upper left', fontsize=24)

ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)

plt.savefig('./scalability_servers_join_queryA.pdf', format='pdf')
