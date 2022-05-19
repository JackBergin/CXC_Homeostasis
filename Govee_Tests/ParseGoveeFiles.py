import matplotlib.pyplot as plt
import csv
  
x = []
y = []
y2 = []

with open('IDFENV.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(row[1])
        y2.append(row[2])

#Removes the first two column values that are not important
x.pop(0)
y.pop(0)
y2.pop(0)

#The following will be used to clean the dates for them to take up less space
size  = len(x)
dataClean = []

for i in range(size):
    dataClean.append(x[i][5:16])

print(dataClean)

cleanGraphDataClean = []
cleanGraphY = []

for i in range(size):
    if(i%8==0):
        cleanGraphDataClean.append(dataClean[i])
        cleanGraphY.append(y[i])

#plt.plot(dataClean, y, color = 'b')
plt.plot(cleanGraphDataClean, cleanGraphY, color = 'b')
plt.xlabel('Time', fontsize = 10)
plt.ylabel('Temperature', fontsize = 10)
plt.title('Temperature over Time IDF environment', fontsize = 20)
plt.show()