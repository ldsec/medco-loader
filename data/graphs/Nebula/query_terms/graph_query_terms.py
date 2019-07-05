import matplotlib.pyplot as plt
import pandas as pd

raw_data_query_one = {
    'x_label':  [2, 3, 4, 5, 10, 25, 50, 100],
    'y1_label': [2412.6+91.6, 3018.4+79.9, 3277.5+72.8, 5101.9+85.5, 8441.5+78.1, 26008.8+97.8,
                 32840.8+89.4, 46092.0+93.4],  # i2b2
    'y2_label': [2789.8-2412.6-91.6, 3168.8-3018.4-79.9, 3454.4-3277.5-72.8,
                 5352.0-5101.9-85.5, 8706.3-8441.5-78.1, 26465.3-26008.8-97.8,
                 33377.3-32840.8-89.4, 46799.7-46092.0-93.4],  # secure protocols
    'y_total':  [2789.8, 3168.8, 3454.4, 5352.0, 8706.3, 26465.3, 33377.3, 46799.7],  # total
}

# convert to seconds
raw_data_query_one['y1_label'] = [x / 1000 for x in raw_data_query_one['y1_label']]
raw_data_query_one['y2_label'] = [x / 1000 for x in raw_data_query_one['y2_label']]
raw_data_query_one['y_total'] = [x / 1000 for x in raw_data_query_one['y_total']]

font = {'family': 'Bitstream Vera Sans',
        'size': 26}

plt.rc('font', **font)

df = pd.DataFrame(raw_data_query_one, raw_data_query_one['x_label'])

fig, ax1 = plt.subplots(1, figsize=(17, 11))
ax1.plot(raw_data_query_one['x_label'], raw_data_query_one['y1_label'], label='MedCo', linewidth=2, ls='--',
         marker='o', markersize=7)
ax1.plot(raw_data_query_one['x_label'], raw_data_query_one['y_total'],
         label='Insecure i2b2', linewidth=2,
         marker='o', markersize=7)

# N = 8
# ind = np.arange(N)  # The x locations for the groups
#
# # Set the bar width
# bar_width = 0.5
#
# # Container of all bars
# bars = []
#
# # Create a bar plot, in position bar_l
# bars.append(ax1.bar(ind,
#                     # using the y1_label data
#                     df['y1_label'],
#                     # set the width
#                     width=bar_width,
#                     label='i2b2',
#                     # with alpha 1
#                     alpha=0.5,
#                     # with color
#                     color='#3232FF'))
#
# # Create a bar plot, in position bar_l
# bars.append(ax1.bar(ind,
#                     # using the y3_label data
#                     df['y2_label'],
#                     # set the width
#                     width=bar_width,
#                     label='Secure protocols',
#                     bottom=df['y1_label'],
#                     # with alpha 1
#                     alpha=0.5,
#                     # with color
#                     color='#1abc78'))
#
# # Set the x ticks with names
# ax1.set_xticks(ind)
# ax1.set_xticklabels(df['x_label'])
# ax1.set_ylim([0, 50])
# ax1.set_xlim([-bar_width, ind[len(ind)-1] + bar_width])
#
# # Labelling
# ax1.text(ind[0] - 0.27, df['y_total'][0] + 0.5,
#          str(round((df['y_total'][0]), 2)), color='black', fontweight='bold')
# ax1.text(ind[1] - 0.27, df['y_total'][1] + 0.5,
#          str(round(df['y_total'][1], 2)), color='black', fontweight='bold')
# ax1.text(ind[2] - 0.27, df['y_total'][2] + 0.5,
#          str(round(df['y_total'][2], 2)), color='black', fontweight='bold')
# ax1.text(ind[3] - 0.27, df['y_total'][3] + 0.5,
#          str(round(df['y_total'][3], 2)), color='black', fontweight='bold')
# ax1.text(ind[4] - 0.27, df['y_total'][4] + 0.6,
#          str(round(df['y_total'][4], 2)), color='black', fontweight='bold')
# ax1.text(ind[5] - 0.27, df['y_total'][5] + 0.6,
#          str(round(df['y_total'][5], 1)), color='black', fontweight='bold')
# ax1.text(ind[6] - 0.27, df['y_total'][6] + 0.5,
#          str(round(df['y_total'][6], 1)), color='black', fontweight='bold')
# ax1.text(ind[7] - 0.27, df['y_total'][7] + 0.5,
#          str(round(df['y_total'][7], 1)), color='black', fontweight='bold')

ax1.set_ylim([0, 50])
ax1.set_xlim([0, 103])

plt.setp(ax1.get_yticklabels()[0], visible=False)

# Set the label and legends
ax1.set_ylabel("Runtime (s)", fontsize=32)
ax1.set_xlabel("Number of query terms", fontsize=32)
plt.legend(loc='upper left', fontsize=32)

ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)

plt.savefig('query_terms.pdf', format='pdf')
