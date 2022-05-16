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
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('IDF Environment Analytics', fontsize = 20)
ax1.plot(dataClean, y,  color = 'b')
ax1.set_ylabel('Temperature (F)', fontsize = 10)
ax2.plot(dataClean, y2,  color = 'r')
ax2.set_xlabel('Time (s)', fontsize = 10)
ax2.set_ylabel('Relative Humidity (%)', fontsize = 10)
plt.autoscale(enable=True, axis='both', tight=None)

#Creates the two humiditity and temperature plots for the XR Wall
fig, (ax3, ax4) = plt.subplots(2, 1)
fig.suptitle('XR Wall Environment Analytics', fontsize = 20)
ax3.plot(dataClean2, yXR,  color = 'b')
ax3.set_ylabel('Temperature (F)', fontsize = 10)
ax4.plot(dataClean2, yXR2,  color = 'r')
ax4.set_xlabel('Time (s)', fontsize = 10)
ax4.set_ylabel('Relative Humidity (%)', fontsize = 10)
plt.autoscale(enable=True, axis='both', tight=None)

#Shows the two figures
plt.show()