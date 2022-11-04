import pdb
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkAgg')


def get_licks_sensor(licking_times):
    lick_threshold = 2.0  # in seconds
    rewards = 0
    bouts = 0
    r_c = 0
    b_c = 0
    # Can make 1-D mask for licking (optional)
    for i, licks in enumerate(licking_times):
        if i < len(licking_times)-1:
            if licking_times[i+1] - licks > lick_threshold:  # If no more licking in next 2.0 s
                if r_c > 5 and b_c:
                    rewards += 1
                    bouts += 1
                else:
                    rewards += 1
                r_c = 0
                b_c = 0
            else:
                if r_c > 20:
                    b_c = True
                    r_c += 1
                else:
                    r_c += 1
    return rewards, bouts


edf_9 = pd.read_pickle('data/RM9_expdf.pickle')  # Have to change all entries to correct rat.
edf_9['rat'] = '9'
edf_10 = pd.read_pickle('data/RM10_expdf.pickle')
edf_10['rat'] = '10'
edf_11 = pd.read_pickle('data/RM11_expdf.pickle')
edf_11['rat'] = '11'
edf_12 = pd.read_pickle('data/RM12_expdf.pickle')
edf_12['rat'] = '12'
edf_13 = pd.read_pickle('data/RM13_expdf.pickle')
edf_13['rat'] = '13'
edf_14 = pd.read_pickle('data/RM14_expdf.pickle')
edf_14['rat'] = '14'
edf_15 = pd.read_pickle('data/RM15_expdf.pickle')
edf_15['rat'] = '15'
edf_16 = pd.read_pickle('data/RM16_expdf.pickle')
edf_16['rat'] = '16'
edf = pd.concat([edf_9, edf_10, edf_11, edf_12, edf_13, edf_14, edf_15, edf_16])
# Column key: 'S' is session, 'dim', 'Date', 'r_start', pos = ['xp', 'yp', 'zp'], 'lick'
# Iterate over unique rat, date, session combinations
c_head = ['Rat', 'Date', 'Session', 'Dim', 'Rew', 'Bout', 'N_Interactions', 'N_Successful']
plot_df = []
for index, content in edf.iterrows():
    rat = content['rat']
    date = content['Date']
    if '25' in date:
        date = 25
    elif '26' in date:
        date = 26
    elif '27' in date:
        date = 27
    elif '28' in date:
        date = 28
    elif '17' in date:
        date=17
    elif '18' in date:
        date = 18
    elif '19' in date:
        date = 19
    else:
        date = 20
    dim = content['dim']
    if 'pidiv' in dim:
        dim = 3
    else:
        dim = 0
    session = content['S']
    n_succ = content['SF'].shape[0]
    num_interactions = len(content['r_start'])  # Get # of trials
    reward_nums, bout_nums = get_licks_sensor(content['lick'])
    pdf = pd.Series([rat, date, session, dim, reward_nums, bout_nums, num_interactions, n_succ])
    plot_df.append(pdf)
pxd = pd.DataFrame(plot_df)
pxd.columns = c_head
pxd.to_csv('metadata_values.csv', index=False)
pdb.set_trace()

# Plots: Color scatters by rat, X-axis is date, Y-axis is Rew, Bout, N-Behaviors

#  3 seperate plots, color by rat
pdb.set_trace()

