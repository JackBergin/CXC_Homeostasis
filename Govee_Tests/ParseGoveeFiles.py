# Imports the necessary plotting libraries
import matplotlib.pyplot as plt
import csv
  
# Initialization of time, temperature, and humidity values
time = []
temp = []
humid = []

time2 = []
temp2 = []
humid2 = []


# Converts values from the csv into lists for graphing
with open('Thermometer 2_export_202205311243.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        time.append(row[0])
        temp.append(row[1])
        humid.append(row[2])

with open('Thermometer 1_export_202205311243.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        time2.append(row[0])
        temp2.append(row[1])
        humid2.append(row[2])

#Removes the first column values that are the labels
time.pop(0)
temp.pop(0)
humid.pop(0)

time2.pop(0)
temp2.pop(0)
humid2.pop(0)

#The following will be used to clean the dates for them to take up less space
size  = len(time)
dateClean = []
for i in range(size):
    dateClean.append(time[i][5:16])

size2  = len(time2)
dateClean2 = []
for i in range(size2):
    dateClean2.append(time2[i][5:16])

# Creates a limited x axis range for tic marks
xAxisTics = []
xAxisTics.append(dateClean[size-1])
xAxisTics.append(dateClean[0])
xAxisTics.append(dateClean[round(size/2)])
xAxisTics.append(dateClean[round(size/4)])
xAxisTics.append(dateClean[round(size*3/4)])


xAxisTics2 = []
xAxisTics2.append(dateClean2[size2-1])
xAxisTics2.append(dateClean2[0])
xAxisTics2.append(dateClean2[round(size2/2)])
xAxisTics2.append(dateClean2[round(size2/4)])
xAxisTics2.append(dateClean2[round(size2*3/4)])


# Casts temperature to float values from string
tempToFloat = []  
humidToFloat = []
for j in range(size):
    tempToFloat.append(float(temp[j]))
    humidToFloat.append(float(humid[j]))

tempToFloat2 = []  
humidToFloat2 = []
for f in range(size2):
    tempToFloat2.append(float(temp2[f]))
    humidToFloat2.append(float(humid2[f]))

# Stylized fonts for the graph's axies
fontAxis = {'family': 'serif',
            'color':  'darkgreen',
            'weight': 'normal',
            'size': 10,
        }

fontTitle = {'family': 'serif',
        'color':  'darkgreen',
        'weight': 'normal',
        'size': 12,
       }

plt.figure(1)
plt.plot(dateClean,tempToFloat, color = '#7C7978')
plt.xlabel('Date and Time', fontdict = fontAxis)
plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontdict = fontAxis)
plt.xticks(xAxisTics)
plt.title('Temperature over Time\n (IDF environment)', fontdict = fontTitle, pad = 10)
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(dateClean, humidToFloat, color = '#7C7978')
plt.xlabel('Date and Time', fontdict = fontAxis)
plt.ylabel('Relative Humidity (%)', fontdict = fontAxis)
plt.xticks(xAxisTics)
plt.title('Relative Humidity over Time\n (IDF environment)', fontdict = fontTitle, pad = 10)
plt.grid(True)
plt.show()

plt.figure(3)
plt.plot(dateClean2,tempToFloat2, color = '#7C7978')
plt.xlabel('Date and Time', fontdict = fontAxis)
plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontdict = fontAxis)
plt.xticks(xAxisTics2)
plt.title('Temperature over Time\n (XR environment)', fontdict = fontTitle, pad = 10)
plt.grid(True)
plt.show()

plt.figure(4)
plt.plot(dateClean2, humidToFloat2, color = '#7C7978')
plt.xlabel('Date and Time', fontdict = fontAxis)
plt.ylabel('Relative Humidity (%)', fontdict = fontAxis)
plt.xticks(xAxisTics2)
plt.title('Relative Humidity over Time\n (XR environment)', fontdict = fontTitle, pad = 10)
plt.grid(True)
plt.show()

'''
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(10,10))

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.9)

ax1.plot(dateClean,tempToFloat, color = '#7C7978')
ax1.set_xlabel('Date and Time', fontdict = fontAxis)
ax1.set_ylabel('Temperature (\N{DEGREE SIGN}F)', fontdict = fontAxis)
ax1.set_xticks(xAxisTics)
ax1.set_title('Temperature over Time\n (IDF environment)', fontdict = fontTitle, pad = 10)
ax1.grid(True)

ax2.plot(dateClean, humidToFloat, color = '#7C7978')
ax2.set_xlabel('Date and Time', fontdict = fontAxis)
ax2.set_ylabel('Relative Humidity (%)', fontdict = fontAxis)
ax2.set_xticks(xAxisTics)
ax2.set_title('Relative Humidity over Time\n (IDF environment)', fontdict = fontTitle, pad = 10)
ax2.grid(True)

ax3.plot(dateClean2,tempToFloat2, color = '#7C7978')
ax3.set_xlabel('Date and Time', fontdict = fontAxis)
ax3.set_ylabel('Temperature (\N{DEGREE SIGN}F)', fontdict = fontAxis)
ax3.set_xticks(xAxisTics2)
ax3.set_title('Temperature over Time\n (XR environment)', fontdict = fontTitle, pad = 10)
ax3.grid(True)

ax4.plot(dateClean2, humidToFloat2, color = '#7C7978')
ax4.set_xlabel('Date and Time', fontdict = fontAxis)
ax4.set_ylabel('Relative Humidity (%)', fontdict = fontAxis)
ax4.set_xticks(xAxisTics2)
ax4.set_title('Relative Humidity over Time\n (XR environment)', fontdict = fontTitle, pad = 10)
ax4.grid(True)


plt.show()
'''