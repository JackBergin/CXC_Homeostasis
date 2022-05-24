# Imports the necessary plotting libraries
import matplotlib.pyplot as plt
import csv
  
# Initialization of time, temperature, and humidity values
time = []
temp = []
humid = []

# Converts values from the csv into lists for graphing
with open('IDFENV.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        time.append(row[0])
        temp.append(row[1])
        humid.append(row[2])

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
for i in range(size):
    if(i%2048==0):
        xAxisTics.append(dateClean[i])

# Casts temperature to float values from string
tempToFloat = []  
for j in range(size):
    tempToFloat.append(float(temp[j]))

# Stylized fonts for the graph's axies
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
        

plt.plot(dateClean, tempToFloat, 'k')
plt.xlabel('Date and Time', fontdict = font)
plt.ylabel('Temperature (Degrees Farenheit)', fontdict = font)
plt.xticks(xAxisTics)
plt.title('Temperature over Time IDF environment', fontdict = font)
plt.show()