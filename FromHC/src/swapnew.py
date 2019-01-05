def swap(List, i, j):
    List[i], List[j] = List[j], List[i]
    

list = [0, 100, 200, 300, 400]
i = 2
j = 3
print("Before swapping:", list[i], list[j])
swap(list, i, j)
print("After swapping:", list[i], list[j])
