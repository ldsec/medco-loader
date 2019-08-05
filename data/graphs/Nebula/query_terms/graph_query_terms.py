import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'Bitstream Vera Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [2, 3, 4, 5, 10, 25, 50, 100],
    'insecure_i2b2': [2412.6+91.6, 3018.4+79.9, 3277.5+72.8, 5101.9+85.5, 8441.5+78.1, 26008.8+97.8,
                      32840.8+89.4, 46092.0+93.4],
    'medco':  [2789.8, 3168.8, 3454.4, 5352.0, 8706.3, 26465.3, 33377.3, 46799.7],
}

# convert to seconds
raw_data['insecure_i2b2'] = [x / 1000 for x in raw_data['y1_label']]
raw_data['medco'] = [x / 1000 for x in raw_data['y_total']]

df = pd.DataFrame(raw_data, raw_data['x_label'])

fig, ax = plt.subplots(1, figsize=(17, 11))
ax.plot(raw_data['x_label'], raw_data['medco'],
        label='MedCo', linewidth=2, ls='--',
        marker='o', markersize=7)
ax.plot(raw_data['x_label'], raw_data['insecure_i2b2'],
        label='Insecure i2b2', linewidth=2,
        marker='o', markersize=7)

ax.set_ylim([0, 50])
ax.set_xlim([0, 103])

plt.setp(ax.get_yticklabels()[0], visible=False)

# Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Number of query terms", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('query_terms.png', format='png')
