import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/crowley-1996.csv')

# Number of people 'low' for the month 1, month 2, etc. for visiting

dog_status = ['control', 'resident']

moods = {'low': 1, 'moderate': 2, 'high': 3}
n_months = 6

index = list(range(1, n_months + 1))

# low = []
# moderate = []
# high = []

for ds in dog_status:

    mood_sums = {}
    mood_mean = {}
    for mood_label in moods.keys():
        mood_sums[mood_label] = []
        mood_mean[mood_label] = []

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
            sum_mood = sum(df[is_mood & is_ds][key_month])

            mood_sums[mood_label].append(sum_mood)

            is_mood = df[key_month] == mood_value
            mean_mood = np.mean(df[is_ds][key_month])

            mood_mean[mood_label].append(mean_mood)

            # if mood == 1:
            #    low.append(sum_actual_mood)
            # elif mood == 2:
            #    moderate.append(sum_actual_mood)
            # else:
            #    high.append

            if ds == 'resident':
                condition_label = ds
            else:
                condition_label = 'visiting'

            title = f'Tension x {condition_label} dog'

            df_fig = pd.DataFrame(mood_sums, mood_mean, index=index)
            ax = df_fig.plot.bar(rot=0)
            ax.set_xlabel('month')
            ax.set_ylabel('frequency')
            ax.set_title(title)
            plt.show()
