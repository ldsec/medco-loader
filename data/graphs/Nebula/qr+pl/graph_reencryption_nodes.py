import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'DejaVu Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [3, 6, 9, 12],
    'DDTreq':  [64.9, 132.25, 189.0,  258.65],
    'DDTcomm': [42.9, 104.7,  161.25, 226.1],
    'DDTexec': [15.7,  15.55,  15.6,   16.45],
    'connDDT': [66.5, 134.55, 191.85, 261.8],
}

# convert to seconds
raw_data['DDTreq'] = [x / 1000 for x in raw_data['DDTreq']]
raw_data['DDTcomm'] = [x / 1000 for x in raw_data['DDTcomm']]
raw_data['DDTexec'] = [x / 1000 for x in raw_data['DDTexec']]
raw_data['connDDT'] = [x / 1000 for x in raw_data['connDDT']]

df = pd.DataFrame(raw_data, raw_data['x_label'])

fig, ax = plt.subplots(1, figsize=(17, 11))
#ax.plot(raw_data['x_label'], raw_data['DDTreq'],
#        label='DDT Request', linewidth=2, ls='--',
#        marker='o', markersize=7)
ax.plot(raw_data['x_label'], raw_data['connDDT'],
        label='Total time', linewidth=2,
        marker='o', markersize=7)
ax.plot(raw_data['x_label'], raw_data['DDTcomm'],
        label='Communication delay', linewidth=2, ls='--',
        marker='o', markersize=7)
ax.plot(raw_data['x_label'], raw_data['DDTexec'],
        label='Computing time', linewidth=2, ls='-.',
        marker='o', markersize=7)

ax.set_ylim([0, 0.4])
ax.set_xlim([3, 13])

plt.setp(ax.get_yticklabels()[0], visible=False)

# # Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Number of nodes", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('loading_re_encryption_nodes.pdf', format='pdf')
