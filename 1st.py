import matplotlib.pyplot as plt

# Learn how to plot a simple graph
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]


plt.plot(x, y, label="First Line") 	# Must use label to allow legend function to recognized it

plt.plot(x2, y2, label="Second Line") 	# Must use label to allow legend function to recognized it

# To label the x-axis
plt.xlabel("Plot Number")

# To label the y-axis
plt.ylabel("Important var")

# To name our title of our graph
plt.title("Interesting Graph\nCheck it out")

# To show the legend
plt.legend()

# Show the graph
plt.show()
