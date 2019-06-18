# Usage: ./hw2_1.sh (inputsize) | python3 hw2_1plot.py

# Read the input size and time
import sys
l = []
for line in iter(sys.stdin.readline, ""):
    line = line.replace("time:", "")
    line = line.replace("sec\n", "")
    l.append(list(map(float,(line.split()))))

# Plot the data       
import matplotlib.pyplot as plt
x = list(map(lambda t: t[0], l))  
y = list(map(lambda t: t[1], l))
plt.plot(x, y, "o")
plt.xlabel('input size')
plt.ylabel('program execution time[s]')
plt.title('Execution time of culculation of matrix product')

# Save as a png file
plt.savefig("Execution_time.png")