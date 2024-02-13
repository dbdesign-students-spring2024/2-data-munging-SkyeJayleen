import csv
import os
newfilepath = os.path.join('data', 'clean_data.csv')

data = []

with open(newfilepath, 'r', encoding = 'utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        data.append(row)

del data[0] # data is now a list containing lists minus the label row.

finalnum = int(data[-1][0])
startingnum = list(range(1880,finalnum,10))
endingnum = list(range(1889,finalnum,10)) + [finalnum]

nummonths = 12*10
finaldecmonths = finalnum - startingnum[-1]
decaverage = []

for i in data:
    chosendata = []
    if i[0][-1] < '9' and i[0] != str(finalnum):
        chosendata += i[1:13]
    elif i[0] == str(finalnum):
        chosendata += i[1:13]
        sum = 0
        for j in chosendata:
            sum += float(j)
        decaverage += [sum / finaldecmonths]
    else:
        chosendata += i[1:13]
        sum = 0
        for j in chosendata:
            sum += float(j)
        decaverage += [sum / nummonths]


print("Average  temperature anomaly in degrees Farenheit by decade:")
for i in range(len(startingnum)):
    print(startingnum[i],"~",endingnum[i],": ", sep = '', end ='')
    print(round(decaverage[i],2))
    if i == len(startingnum) - 1:
        print("The final 'decade' may not be comprehensive data; please look at the number of years data was measured.")