import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

# open .CSV file
data = pd.read_csv("cs4222_students_list.csv")
print(data.to_string())

#A

# sort by last name
start = time.time()
dataA = data.sort_values('Last Name')
end = time.time()
time_sort = end-start

dataA = dataA.reset_index(drop=True)
print(dataA.to_string())

#B

# add columns
dataB = dataA
dataB["1module code"] = ""
dataB["1module title"] = ""
dataB["1mark"] = 0
dataB["2module code"] = ""
dataB["2module title"] = ""
dataB["2mark"] = 0
dataB["3module code"] = ""
dataB["3module title"] = ""
dataB["3mark"] = 0
dataB
print(dataB.to_string())

# fill columns of team members
GroupUID = ['#23358459','#23370211','#23362995','#23362235']
for i in range(0, len(dataB.UID)):
    if dataB.iloc[i]['UID'] in GroupUID:
        dataB.at[i, '1module code'] = 'CS4221'
        dataB.at[i, '1module title'] = 'Foundations of Coumputer Science 1'
        dataB.at[i, '2module code'] = 'CS4222'
        dataB.at[i, '2module title'] = 'Software Development'
        dataB.at[i, '3module code'] = 'CS4141'
        dataB.at[i, '3module title'] = 'Introduction to Programming'
    dataB.at[i, '1mark'] = number = random.randint(1, 100)
    dataB.at[i, '2mark'] = number = random.randint(1, 100)
    dataB.at[i, '3mark'] = number = random.randint(1, 100)
print(dataB.to_string())

# C

# find top 3 students in team for each module
start = time.time()
dataC = dataB.loc[dataB['UID'].isin(GroupUID)]
dataC1 = dataC.nlargest(3, '1mark')
dataC2 = dataC.nlargest(3, '2mark')
dataC3 = dataC.nlargest(3, '3mark')
end = time.time()
time_search = end-start

print(dataC.to_string())

#D

# plot sort time vs search time
colour = ['pink', 'lightskyblue']
mpl.bar(("Sort Algorithim","Search Algorithim"), (time_sort, time_search), color = colour)
mpl.ylabel("Time in Seconds")
mpl.show()

print("\n" + str(time_sort) + "\n" + str(time_search))

#E 

# plot distribution of marks across modules
index = np.arange(3)
bar_width = 0.25

fig, ax = mpl.subplots()
CS4221 = ax.bar(index, dataC1["1mark"], bar_width,
                label="CS4221")

CS4222 = ax.bar(index+bar_width, dataC2["2mark"],
                 bar_width, label="CS4222") 

CS4141 = ax.bar(index+bar_width+bar_width, dataC3["3mark"],
                 bar_width, label="CS4141")

ax.set_ylabel('Marks')
ax.set_title('Mark distribution')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(["1st", "2nd", "3rd"])
ax.legend()

mpl.show()

