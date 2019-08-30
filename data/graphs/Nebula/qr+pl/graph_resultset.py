import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'DejaVu Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [52,451,940,1511], # medco-connector-i2b2-PSM
    'insecure_i2b2': [13719.12,100845.4,201857.5,312083.8],
    'medco':  [14052.88,101787.8,203333.4,314200.2],
}

# convert to seconds
raw_data['insecure_i2b2'] = [x / 1000 for x in raw_data['insecure_i2b2']]
raw_data['medco'] = [x / 1000 for x in raw_data['medco']]

df = pd.DataFrame(raw_data, raw_data['x_label'])

fig, ax = plt.subplots(1, figsize=(17, 11))
ax.plot(raw_data['x_label'], raw_data['medco'],
        label='Encrypted', linewidth=2, ls='--',
        marker='o', markersize=7)
ax.plot(raw_data['x_label'], raw_data['insecure_i2b2'],
        label='Unencrypted', linewidth=2,
        marker='o', markersize=7)

ax.set_ylim([0, 330])
ax.set_xlim([40,1700])

plt.setp(ax.get_yticklabels()[0], visible=False)

# # Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Number of matching patients per node", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

for i in range(len(raw_data['x_label'])):
        plt.annotate('(%+.2f)'%(raw_data['medco'][i]-raw_data['insecure_i2b2'][i]),xy=(raw_data['x_label'][i],raw_data['medco'][i]),xytext=(raw_data['x_label'][i]+10,raw_data['medco'][i]-10))

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('result_set.pdf', format='pdf')
