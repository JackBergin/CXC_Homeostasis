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
y2.pop()


plt.plot(x[0:100], y[0:100], color = 'b')
plt.xlabel('Time', fontsize = 10)
plt.ylabel('Temperature', fontsize = 10)
plt.title('Temperature over Time IDF environment', fontsize = 20)
plt.show()