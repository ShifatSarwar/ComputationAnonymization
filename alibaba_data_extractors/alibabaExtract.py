import pandas as pd
# Lowest possible data for train test without dropping task type 7 is 1000
train = pd.read_csv('batch_task.csv', usecols=[0,1,2,3,4,5,6,7,8], names=['taskName', 'instanceNum', 'jobName', 'taskType', 'status', 'timeTaken', 'endTime', 'cpus', 'mem'])
# train = pd.read_csv('dataList/tests/.csv')

# Extracts the first 2000 data from Alibaba Dataset batch_task.csv file
# We drop unnecessary columns like Job Name, Status, and Task Name
# We will use task type to identify computation rather than specific tasks.
x = train
x = x.dropna()
x = x.drop(columns=['jobName'])
x = x.drop(columns=['status'])
x = x.drop(columns=['taskName'])

g = x.loc[x['taskType'] == 1]
g = g.head(2000)
g.to_csv('dataList/graph01.csv')

g = x.loc[x['taskType'] == 3]
g = g.head(2000)
g.to_csv('dataList/graph02.csv')

g = x.loc[x['taskType'] == 4]
g = g.head(2000)
g.to_csv('dataList/graph03.csv')

g = x.loc[x['taskType'] == 5]
g = g.head(2000)
g.to_csv('dataList/graph04.csv')

g = x.loc[x['taskType'] == 6]
g = g.head(2000)
g.to_csv('dataList/graph05.csv')

g = x.loc[x['taskType'] == 8]
g = g.head(2000)
g.to_csv('dataList/graph06.csv')

g = x.loc[x['taskType'] == 9]
g = g.head(2000)
g.to_csv('dataList/graph07.csv')

g = x.loc[x['taskType'] == 10]
g = g.head(2000)
g.to_csv('dataList/graph08.csv')

g = x.loc[x['taskType'] == 11]
g = g.head(2000)
g.to_csv('dataList/graph09.csv')

g = x.loc[x['taskType'] == 12]
g = g.head(2000)
g.to_csv('dataList/graph10.csv')

print("Done")

