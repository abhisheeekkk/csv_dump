#Better to open in google colab, because that's where I edited this. Link --->>> https://colab.research.google.com/drive/1tD4zFdu8eOaFOBSAyWAF3kMiU2MCUBGZ#scrollTo=KSfH6psMPcvJ&line=14&uniqifier=1


import pandas as pd
import pytz


#task1-->> Converting GPS time to IST time
url = 'https://raw.githubusercontent.com/abhisheeekkk/csv_dump/main/raw_triggers.csv'

df = pd.read_csv(url)

df.iloc[:,1] = pd.to_datetime(df.iloc[:,1], format='%Y-%m-%d %H:%M:%S')

ist = pytz.timezone('Asia/Kolkata')

df.iloc[:,1] = df.iloc[:,1].dt.tz_localize('UTC').dt.tz_convert(ist)

# save the updated dataframe to a new CSV file
df.to_csv('filename_ist2.csv', index=False)

#task2-->> counting the number of triggers in the CSV file and storing it in the counter variable, total count is 1075.
url2 = 'https://raw.githubusercontent.com/abhisheeekkk/csv_dump/main/filename_ist2.csv'

df2 = pd.read_csv(url2)

counter = 0
prev_value = 0

# iterate through the values in the eleventh column
for value in df2.iloc[:,10]:
    # check if the value is a trigger
    if value == 1700 and prev_value == 1500:
        counter += 1
    # store the previous value for comparison
    prev_value = value

# print the trigger count
print('Number of triggers:', counter)
