import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'Bitstream Vera Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [15000, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000],
    'medco':  [1.84, 2.5, 4.9, 7.9, 10.86, 13.76, 16.79, 19.74, 22.4, 25, 27.85],
}

df = pd.DataFrame(raw_data, raw_data['x_label'])

fig, ax = plt.subplots(1, figsize=(17, 11))
ax.plot(raw_data['x_label'], raw_data['medco'],
        label='Encryption time', linewidth=2, ls='--',
        marker='o', markersize=7)

ax.set_ylim([0, 35])
ax.set_xlim([0, 220000])

plt.setp(ax.get_yticklabels()[0], visible=False)

# Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Number of terms", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

labels = [item.get_text() for item in ax.get_xticklabels()]
labels[1] = '0'
labels[1] = '25K'
labels[2] = '50K'
labels[3] = '75K'
labels[4] = '100K'
labels[5] = '125K'
labels[6] = '150K'
labels[7] = '175K'
labels[8] = '200K'

ax.set_xticklabels(labels)

plt.savefig('encryption.png', format='png')
