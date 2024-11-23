import scipy
import numpy as np

def relu(x):
    return max(0, x)

x = np.array([[2,0,4], [1,-1,0], [-2,3,1]])
c1 = np.array([[0,-2,1],[2,-3,0],[2,-3,-1]])
c2 = np.array([[0,-2,1],[2,-3,0],[2,-3,-1]])

y1 = scipy.signal.convolve2d(x, c1, mode='same', boundary='fill', fillvalue=0)

print(x)
print(c1)
print(y1)

vec_relu = np.vectorize(relu)
o1 = vec_relu(y1)
print(o1)

y2 = scipy.signal.convolve2d(o1, c2, mode='same')
print(y2)

o2 = vec_relu(y2)
print(y2)