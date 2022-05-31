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

def cleanData(time, temp, humid):
    #Removes the first column values that are the labels
    time.pop(0)
    temp.pop(0)
    humid.pop(0)
    
    #The following will be used to clean the dates for them to take up less space
    size  = len(time)
    dateClean = []
    for i in range(size):
        dateClean.append(time[i][5:16])
    
    # Creates a limited x axis range for tic marks
    xAxisTics = []
    xAxisTics.append(dateClean[size-1])
    xAxisTics.append(dateClean[0])
    xAxisTics.append(dateClean[round(size/2)])
    xAxisTics.append(dateClean[round(size/4)])
    xAxisTics.append(dateClean[round(size*3/4)])
    
    # Casts temperature to float values from string
    tempToFloat = []  
    humidToFloat = []
    for j in range(size):
        tempToFloat.append(float(temp[j]))
        humidToFloat.append(float(humid[j]))

    return tempToFloat,humidToFloat,dateClean,xAxisTics

    

def plotTempIDF():
    tempToFloat, humidToFloat, dateClean, xAxisTics = cleanData(time, temp, humid)
    plt.figure(1)
    plt.plot(dateClean,tempToFloat, color = '#7C7978')
    plt.xlabel('Date and Time', fontdict = fontAxis)
    plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontdict = fontAxis)
    plt.xticks(xAxisTics)
    plt.title('Temperature over Time\n (IDF environment)', fontdict = fontTitle, pad = 10)
    plt.grid(True)
    plt.show()

def plotHumidityIDF():
    tempToFloat, humidToFloat, dateClean, xAxisTics = cleanData(time, temp, humid)
    plt.figure(2)
    plt.plot(dateClean, humidToFloat, color = '#7C7978')
    plt.xlabel('Date and Time', fontdict = fontAxis)
    plt.ylabel('Relative Humidity (%)', fontdict = fontAxis)
    plt.xticks(xAxisTics)
    plt.title('Relative Humidity over Time\n (IDF environment)', fontdict = fontTitle, pad = 10)
    plt.grid(True)
    plt.show()

def plotTempXR():
    tempToFloat2, humidToFloat2, dateClean2, xAxisTics2 = cleanData(time2, temp2, humid2)
    plt.figure(3)
    plt.plot(dateClean2,tempToFloat2, color = '#7C7978')
    plt.xlabel('Date and Time', fontdict = fontAxis)
    plt.ylabel('Temperature (\N{DEGREE SIGN}F)', fontdict = fontAxis)
    plt.xticks(xAxisTics2)
    plt.title('Temperature over Time\n (XR environment)', fontdict = fontTitle, pad = 10)
    plt.grid(True)
    plt.show()

def plotHumidityXR():
    tempToFloat2, humidToFloat2, dateClean2, xAxisTics2 = cleanData(time2, temp2, humid2)
    plt.figure(4)
    plt.plot(dateClean2, humidToFloat2, color = '#7C7978')
    plt.xlabel('Date and Time', fontdict = fontAxis)
    plt.ylabel('Relative Humidity (%)', fontdict = fontAxis)
    plt.xticks(xAxisTics2)
    plt.title('Relative Humidity over Time\n (XR environment)', fontdict = fontTitle, pad = 10)
    plt.grid(True)
    plt.show()

plotTempIDF()
plotHumidityIDF()
plotTempXR()
plotHumidityXR()