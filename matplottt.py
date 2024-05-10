import numpy as np
import matplotlib.pyplot as plt

w = [1, 2, 3, 4, 5, 6, 7, 8]  # Using square brackets to define a list
w1 = [i * 2 for i in w]       # Using list comprehension to generate w1
w2 = [i * 3 for i in w]       # Using list comprehension to generate w2

print(w)
print(w1)
print(w2)

plt.plot(w, w2, "H")
plt.xlabel("list w")
plt.ylabel("list w2")  # Fixed the ylabel label
plt.show()
