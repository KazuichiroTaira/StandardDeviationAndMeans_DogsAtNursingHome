import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

DATA_FOLDER = 'data'
FIG_FOLDER = 'fig'

os.makedirs(FIG_FOLDER, exist_ok=True)

data_file = os.path.join(DATA_FOLDER, 'crowley-1996.csv')
df = pd.read_csv(data_file)

# Number of people 'low' for the month 1, month 2, etc. for visiting

dog_status = ['control', 'resident']

moods = {'low': 1, 'moderate': 2, 'high': 3}
n_months = 6

index = list(range(1, n_months + 1))

# low = []
# moderate = []
# high = []

for ds in dog_status:

    data = {}
    labels = ['low', 'moderate', 'high', 'mean']
    for label in labels:
        data[label] = []

    # data = {'low': [], 'moderate': [], 'high': [], 'mean':[]}

    is_ds = df['condition'] == ds

    # sum_m1 = sum(df[is_low&is_control]['m1'])
    # sum_m2 = sum(df[is_low&is_control]['m2'])
    # low.append(sum_m1)
    # low.append(sum_m2)

    for i in range(n_months):
        key_month = 'm' + str(i + 1)

        # is_low = df[key_month] == 1
        # sum_low = sum(df[is_low&is_control][key_month])
        # low.append(sum_low)

        for (mood_label, mood_value) in moods.items():

            is_mood = df[key_month] == mood_value
            count_mood = len(df[is_mood & is_ds][key_month])

            data[mood_label].append(count_mood)

        mean_mood = np.mean(df[is_ds][key_month])

        data['mean'].append(mean_mood)

    if ds == 'resident':
        condition_label = ds
    else:
        condition_label = 'visiting'

    title = f'Tension x {condition_label} dog'

    df_fig = pd.DataFrame(data, index=index)
    ax = df_fig.plot.bar(rot=0)
    ax.set_xlabel('month')
    ax.set_ylabel('frequency')
    ax.set_title(title)

    fig_name = f'{condition_label}.pdf'
    fig_file = os.path.join(FIG_FOLDER, fig_name)
    plt.savefig(fig_file)
