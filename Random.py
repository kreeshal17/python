import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
import random
random.seed(5)
print(random.random())
print(random.random())
import random
sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
