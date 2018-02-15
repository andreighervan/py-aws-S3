from matplotlib import pyplot as plt
from matplotlib import style
population_ages=[22,55,60,45,21,22,34,42,42,99,110,110,44]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.title('Histogram')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True,color='k')
plt.show()