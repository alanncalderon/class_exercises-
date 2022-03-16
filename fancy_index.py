import numpy as np
a = np.zeros((8,3), dtype = np.int16)
for i in range(8):
    a[i]= i
print(a)
fancy_index = [1,3,5]
print(f"a[fancy] = \n {a[fancy_index]}")
# it wrods with negative numbers
fancy2= [-1,-2,-4]
print(f"a [fancy2]= \n{a [fancy2]}")