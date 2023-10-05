import mathplotlib.py plot as plt
#pass the x and y cordinates of the bars to the 
#function the label argument given a label to the data
plt.bar([1,3,5,7,9],[5,2,7,8,2],label="data 1")
plt.legend()


#the following commands add labels in your figure
plt.xlabel('x values')
plt.ylabel('height')
plt.title('vertical bar chart')
plt.show()
