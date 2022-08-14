from matplotlib import pyplot as plt
from matplotlib import style 
import numpy as np #used for loading the csv values 

style.use('ggplot')

x,y = np.loadtxt('C:\\Users\\Rohans PC\\OneDrive\\Desktop\\AI\\test.csv', unpack = True, delimiter = ',', skiprows = 1) #skiprows = 1 (skips the first header row filled with stings)
plt.plot(x,y)

plt.title('Epic Chart') #name of the title
plt.ylabel('Y axis') #name of the Y axis plot 
plt.xlabel('X axis') #name of the X axis plot

plt.show()

