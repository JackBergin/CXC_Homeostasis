import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('IDFENV.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append(row[2])
  
print(x)
print(y)

#plt.bar(x, y, color = 'g')
##plt.xlabel('Time')
#plt.ylabel('Temperature')
#plt.title('Temperature over Time IDF environment')
#plt.legend()
#plt.show()