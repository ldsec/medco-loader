import matplotlib.pyplot as plt
import pandas as pd

font = {'family': 'DejaVu Sans',
        'size': 26}
plt.rc('font', **font)

raw_data = {
    'x_label':  [2.37*3, 3.17*3, 4.75*3, 9.8*3], # medco-connector-i2b2-PSM
    'insecure_i2b2': [73440.85,98020.15,151112.55,312083.8],
    'medco':  [75592.25,100206.1,153244.2,314200.2],
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

ax.set_ylim([0, 400])
ax.set_xlim([7, 30])

plt.setp(ax.get_yticklabels()[0], visible=False)

# # Set the label and legends
ax.set_ylabel("Runtime (s)", fontsize=32)
ax.set_xlabel("Size of the database (Billions of variables)", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

for i in range(len(raw_data['x_label'])):
        plt.annotate('(%+.2f)'%(raw_data['medco'][i]-raw_data['insecure_i2b2'][i]),xy=(raw_data['x_label'][i],raw_data['medco'][i]),xytext=(raw_data['x_label'][i]-0.2*i*i,raw_data['medco'][i]-20-7*i-4*i*i+3*i*i*i))

ax.tick_params(axis='x', labelsize=32)
ax.tick_params(axis='y', labelsize=32)

plt.savefig('db_scalability.pdf', format='pdf')
