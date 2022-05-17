import matplotlib.pyplot as plt
import csv
  
x = []
y = []
y2 = []

x2 = []
yXR = []
yXR2 = []

with open('IDFENV.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(row[1])
        y2.append(row[2])

with open('XRENV.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x2.append(row[0])
        yXR.append(row[1])
        yXR2.append(row[2])

#Removes the first two column values that are not important
x.pop(0)
y.pop(0)
y2.pop(0)

x2.pop(0)
yXR.pop(0)
yXR2.pop(0)

#The following will be used to clean the dates for them to take up less space
size  = len(x)
size2 = len(x2)
dataClean = []
dataClean2 = []

for i in range(size):
    dataClean.append(x[i][5:16])

for j in range(size2):
    dataClean2.append(x2[j][5:16])

#Creates the two humiditity and temperature plots for the IDF
plt.rcParams["figure.figsize"] = (12,8.5)

#fig.subplottitle('IDF Environment Analytics', fontsize = 20)
for k in range(size):
    plt.plot(dataClean[k], k,  color = 'b')
plt.ylabel('Temperature (F)', fontsize = 10)
plt.xlabel('Time (s)', fontsize = 10)
plt.ylim(0,100)
#Shows the two figures
plt.show()