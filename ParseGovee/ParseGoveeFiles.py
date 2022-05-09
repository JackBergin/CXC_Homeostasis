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


#!/usr/bin/env python
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

datatype=[('index',numpy.float32), ('floati',numpy.float32), 
        ('floatq',numpy.float32)]
filename='bigdata.bin'

def main():
    data = numpy.memmap(filename, datatype, 'r') 
    plt.plot(data['floati'],data['floatq'],'r,')
    plt.grid(True)
    plt.title("Signal-Diagram")
    plt.xlabel("Sample")
    plt.ylabel("In-Phase")
    plt.savefig('foo2.png')

if __name__ == "__main__":
    main()  