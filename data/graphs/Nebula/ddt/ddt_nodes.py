import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'Bitstream Vera Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [3, 6, 9, 12],
    'medco':  [33.4, 58, 74.8, 98],
}

df = pd.DataFrame(raw_data, raw_data['x_label'])

fig, ax = plt.subplots(1, figsize=(17, 11))
ax.plot(raw_data['x_label'], raw_data['medco'],
        label='Tagging time', linewidth=2, ls='--',
        marker='o', markersize=7)

plt.setp(ax.get_yticklabels()[0], visible=False)

# Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Number of nodes", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('ddt_nodes.png', format='png')
