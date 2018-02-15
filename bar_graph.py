from matplotlib import pyplot as plt
from matplotlib import style

plt.bar([1,3,5,7,9],[5,3,7,8,2],label="Example one")
plt.bar([1,3,5,7,9],[5,3,7,8,2],label="Example two",color='g')
plt.title('Info')
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.legend()
plt.grid(True,color='k')
plt.show()