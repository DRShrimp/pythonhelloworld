# x = [4, 3, 2, 6, 5, 8, 19, 4, 7]

newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)