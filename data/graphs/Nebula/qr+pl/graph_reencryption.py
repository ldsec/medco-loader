import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'DejaVu Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [1, 5, 10, 25, 50, 100],
    'DDTreq':  [18.54, 42.2,  65.8,  118.75, 200.85, 370.7],
    'DDTcomm': [11.08, 26.98, 43.36,  80.5,  138.35, 260.1],
    'DDTexec': [2,      8.84, 15.76,  28.45,  49.65,  92.25],
    'connDDT': [19.76, 43.6,  67.56,  121.7, 205.5,  378.95],
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
ax.set_xlim([0, 100])

plt.setp(ax.get_yticklabels()[0], visible=False)

# # Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Number of variables", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('loading_re_encryption.pdf', format='pdf')
