from matplotlib import pyplot as plt
from matplotlib import style
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
plt.scatter(x,y,label='skitscat',color='k')
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True,color='k')
plt.show()