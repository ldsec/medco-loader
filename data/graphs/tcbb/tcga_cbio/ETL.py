import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

raw_data = {
    'x_label':  ['1000', '2000', '4000', '8000'],
    'parsing_ontology': [121.51, 121.51, 121.51, 121.51],          # Parsing Ontology
    'ontology_encryption': [37.94, 37.94, 37.94, 37.94],           # Encryption
    'ontology_re_encryption': [172.41, 172.41, 172.41, 172.41],    # Data tagging
    'loading_ontology': [62.26, 62.26, 62.26, 62.26],              # Loading Ontology
    'parsing_dataset': [21.23, 45.36, 87.43, 168.73],              # Parsing Dataset
    'loading_dataset': [9.91, 21, 42.1, 87.3],                     # Loading Dataset
    'total': [425.3, 460.5, 523.6, 650.1],                         # Total
}

font = {'family': 'Bitstream Vera Sans',
        'size': 26}

plt.rc('font', **font)

df = pd.DataFrame(raw_data, raw_data['x_label'])

N = 4
ind = np.arange(N)  # The x locations for the groups

# Create the general blog and the "subplots" i.e. the bars
fig, ax1 = plt.subplots(1, figsize=(14, 12))

# Set the bar width
bar_width = 0.5

ax1.bar(ind, df['parsing_ontology'], width=bar_width, label='Parsing ontology', alpha=0.7,
        color='#1C303C', edgecolor='black')
ax1.bar(ind, df['ontology_encryption'], width=bar_width, label='Ontology encryption', bottom=df['parsing_ontology'],
        alpha=0.7, color='#309F9B', edgecolor='black')

ax1.bar(ind, df['ontology_re_encryption'], width=bar_width, bottom=[x1 + x2 for
                                                                    x1, x2 in zip(df['parsing_ontology'],
                                                                                  df['ontology_encryption'])],
        label="Ontology deterministic re-encryption", alpha=0.7, color='#51536D', edgecolor='black')

ax1.bar(ind, df['loading_ontology'], width=bar_width, bottom=[x1 + x2 + x3 for
                                                              x1, x2, x3 in zip(df['parsing_ontology'],
                                                                                df['ontology_encryption'],
                                                                                df['ontology_re_encryption'])],
        label="Loading ontology to SPU database", alpha=0.7, color='#8293BE', edgecolor='black')

ax1.bar(ind, df['parsing_dataset'], width=bar_width, bottom=[x1 + x2 + x3 + x4 for
                                                             x1, x2, x3, x4 in zip(df['parsing_ontology'],
                                                                                   df['ontology_encryption'],
                                                                                   df['ontology_re_encryption'],
                                                                                   df['loading_ontology'])],
        label="Parsing dataset", alpha=0.7, color='#5B9E63', edgecolor='black')

ax1.bar(ind, df['loading_dataset'], width=bar_width, bottom=[x1 + x2 + x3 + x4 + x5 for
                                                             x1, x2, x3, x4, x5 in zip(df['parsing_ontology'],
                                                                                       df['ontology_encryption'],
                                                                                       df['ontology_re_encryption'],
                                                                                       df['loading_ontology'],
                                                                                       df['parsing_dataset'])],
        label="Loading dataset to SPU database", alpha=0.7, color='#826385', edgecolor='black')


# Set the x ticks with names
ax1.set_xticks(ind)
ax1.set_xticklabels(df['x_label'])
ax1.set_ylim([0, 1200])
ax1.set_xlim([-bar_width, ind[2] + 3*bar_width])

# Labelling
ax1.text(ind[0] - 0.21, df['total'][0]+8,
         str(df['total'][0]), color='black', fontweight='bold')
ax1.text(ind[1] - 0.21, df['total'][1]+8,
         str(df['total'][1]), color='black', fontweight='bold')
ax1.text(ind[2] - 0.21, df['total'][2]+8,
         str(df['total'][2]), color='black', fontweight='bold')
ax1.text(ind[3] - 0.21, df['total'][3]+8,
         str(df['total'][3]), color='black', fontweight='bold')

# Set the label and legends
ax1.set_ylabel("Runtime (s)", fontsize=32)
ax1.set_xlabel("#patients per site", fontsize=32)
plt.legend(loc='upper left', fontsize=24)

ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)

plt.axhline(y=394.12, color='k', linestyle='--')

plt.savefig('./ETL.pdf', format='pdf')
