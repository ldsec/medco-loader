import matplotlib.pyplot as plt
import pandas as pd
import pylab as pyl
import numpy as np

font = {'family': 'DejaVu Sans',
        'size': 12}

#plt.rc('text', usetex=True)
plt.rc('font', **font)

# removeX = MAX(raw_data_query_one[:8]) - raw_data_query_one[:8] (not in percentage)
#removeX1 = 0
#removeX2 = 21.882 - 0.02 - 0.076 - 0.026 - 21.313 - 0.25 - 0.092 - 0.03
#removeX3 = 21.882 - 0.02 - 0.077 - 0.027 - 20.127 - 1.3 - 0.139 - 0.03
removeX1 = 77362.85-226.1-16.45-74698.2-411.55-70.5-1283.95-66.85-931.4 #This is negative, so it is omitted
#print(removeX1)
# min value= 0.02
#raw_data_query = {'y_label': ['SPU1', 'SPU2', 'SPU3'],                      # Servers
#                  'empty': [0, 0, 0],                                       # Empty
#                  'query_parsing': [0.02, 0.02, 0.02],                      # Query Parsing
#                  'query_tagging_comm': [0.074, 0.076, 0.077],              # Query Tagging Communication
#                  'query_tagging': [0.027, 0.026, 0.027],                   # Query Tagging
#                  'i2b2_query': [20.235+1.4, 21.313+0.25, 20.127+1.3],      # I2B2 query
#                  'encrypted_flag_ret':  [0.096, 0.092, 0.139],             # Encrypted flag retrieval
#                  'aggregation': [0.03, 0.03, 0.03],                        # Aggregation
#                  'waiting': [removeX1, removeX2, removeX3],                # Waiting
#                  'shuffling':   [0.02, 0.02, 0.02],                        # Shuffling
#                  'key_switching': [0.02, 0.02, 0.02],                      # Key Switching
#                  'extra': [22.030-21.882, 21.892-21.882, 21.961-21.882],   # Extra processing
#                  }
raw_data_query = {'y_label': ['Computing node'],                      # Servers
                  'empty': [0],                                       # Empty
                  'query_tagging_comm': [226.1],              # Query Tagging Communication
                  'query_tagging': [16.45],                   # Query Tagging
                  'i2b2_query': [74698.2],      # I2B2 query
                  'encrypted_flag_ret':  [411.55],             # Encrypted flag and patient list retrieval
                  'aggregation': [70.5],                        # Aggregation
                  'masking' : [931.4],                      
                  #'waiting': [removeX1],                # Waiting
                  'key_switching': [1283.95+66.85],                      # Key Switching
                  #'extra': [22.030-21.882, 21.892-21.882, 21.961-21.882],   # Extra processing
                  }
df = pd.DataFrame(raw_data_query, raw_data_query['y_label'])

# Create the general plot and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(300, 30))

# Set the bar width
bar_width = 0.5

# Positions of the left bar-boundaries
bar_l = pos = pyl.arange(len(df['y_label']))+.3 + (bar_width / 2)

# Positions of the y-axis ticks (center of the bars as bar labels)
tick_pos = bar_l

# BAR/DATA

ax1.barh(bar_l, df['empty'], bar_width, label='Re-encryption Communication', alpha=0.5, hatch='//', color='white', edgecolor='black')

#ax1.barh(bar_l, df['query_parsing'], bar_width, label='Query parsing', alpha=0.8, color='#664b39', edgecolor='black')

ax1.barh(bar_l, df['query_tagging_comm'], bar_width, left=df['empty'], label='', alpha=0.5, hatch='//',
         color='#f2d70e', edgecolor='black')

ax1.barh(bar_l, df['query_tagging'], bar_width,
         left=df['query_tagging_comm'],
         label='Query Re-encryption', alpha=0.5, color='#f2d70e', edgecolor='black')

ax1.barh(bar_l, df['i2b2_query'], bar_width,
         left=[x1 + x2 for x1, x2 in zip(df['query_tagging_comm'], df['query_tagging'])],
         label='Database query', alpha=0.5, color='#654321', edgecolor='black')

ax1.barh(bar_l, df['encrypted_flag_ret'], bar_width,
         left=[x1 + x2 + x3 for x1, x2, x3 in zip(df['query_tagging_comm'],
                                                           df['query_tagging'], df['i2b2_query'])],
         label='Result list and encrypted flag retrieval', alpha=0.5, color='#4C8E8B', edgecolor='black')

ax1.barh(bar_l, df['aggregation'], bar_width,
         left=[x1 + x2 + x3 + x4 for x1, x2, x3, x4 in zip(
             df['query_tagging_comm'], df['query_tagging'], df['i2b2_query'],
             df['encrypted_flag_ret'])],
         label='Homomorphic aggregation', alpha=0.5, color='#3232FF', edgecolor='black')

ax1.barh(bar_l, df['masking'], bar_width,
         left=[x1 + x2 + x3 + x4 + x5 for x1, x2, x3, x4, x5 in zip(
             df['query_tagging_comm'], df['query_tagging'], df['i2b2_query'],
             df['encrypted_flag_ret'], df['aggregation'])],
         label='Result list masking', alpha=0.5, color='#92f442', edgecolor='black')

#ax1.barh(bar_l, df['waiting'], bar_width,
#         left=[x1 + x2 + x3 + x4 + x5 + x6 for x1, x2, x3, x4, x5, x6 in zip(
#             df['query_tagging_comm'], df['query_tagging'], df['i2b2_query'],
#             df['encrypted_flag_ret'], df['aggregation'], df['masking'])],
#         label='Synchronization', alpha=0.5, color='black', edgecolor='black')

#ax1.barh(bar_l, df['shuffling'], bar_width,
#         left=[x1 + x2 + x3 + x4 + x5 + x6 + x7 for x1, x2, x3, x4, x5, x6, x7 in zip(
#             df['query_parsing'], df['query_tagging_comm'], df['query_tagging'], df['i2b2_query'],
#             df['encrypted_flag_ret'], df['aggregation'], df['waiting'])],
#         label='Result shuffling', alpha=0.5, color='#92f442', edgecolor='black')

ax1.barh(bar_l, df['key_switching'], bar_width,
         left=[x1 + x2 + x3 + x4 + x5 + x6 for x1, x2, x3, x4, x5, x6 in zip(
             df['query_tagging_comm'], df['query_tagging'], df['i2b2_query'],
             df['encrypted_flag_ret'], df['aggregation'], df['masking'])],
         label='Result key-switching', alpha=0.5, color='#d1101d', edgecolor='black')

#ax1.barh(bar_l, df['extra'], bar_width,
#         left=[x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 for x1, x2, x3, x4, x5, x6, x7, x8, x9 in zip(
#             df['query_parsing'], df['query_tagging_comm'], df['query_tagging'], df['i2b2_query'],
#             df['encrypted_flag_ret'], df['aggregation'], df['waiting'], df['shuffling'], df['key_switching'])],
#         label='Extra processing', alpha=0.5, edgecolor='black', hatch='x', color='white')


# Set the y ticks with names
plt.yticks(tick_pos, df['y_label'])
ax1.xaxis.grid(False)
plt.xticks(np.arange(0, 78000, 1000))

# Set the label and legends
ax1.set_xlabel("Runtime (ms)", fontsize=72)
plt.legend(loc='upper center', ncol=2, fontsize=72)

ax1.tick_params(axis='x', labelsize=60)
ax1.tick_params(axis='y', labelsize=72)

# Set a buffer around the edge
plt.ylim([0, 2])
plt.xlim([0, 78000])

#plt.axvline(x=21.882, ymin=0, ymax=10, linewidth=1, color='k')
plt.savefig('timeline_medco.pdf', format='pdf')