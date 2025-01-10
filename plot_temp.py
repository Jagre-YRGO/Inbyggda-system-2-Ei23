import matplotlib.pyplot as plt

print('welcome to temp_plot!')

#open file with values and read into list
f = open('temps.csv',mode='r')
temps = []

for line in f:
    temps.append(float(line))
print(temps)

f.close()

#plot values
plt.plot(temps,ls=":")
plt.ylabel('temp [℃]')
plt.xlabel('time [1/10 s]')
plt.show()

#exit program
print('leaving program - good bye!')