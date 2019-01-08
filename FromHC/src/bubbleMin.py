"""
Given a integer list and a index (denoted as startIdx), 
find the min value's index (denoted as minIdx) after startIdx (inclusive), 
then swap the values at startIdx and minIdx.
You should not create new list, and all the operations are on the original list
Try to import your previous swap module to do the swapping operation.

for example:
list: 3,2,1,5
startIdx: 1
modified list: 3,1,2,5

list: 3,2,1,5
startIdx: 0
modified list: 1,2,3,5
"""

def swap(List, i, j):
    List[i], List[j] = List[j], List[i]

def bubbleMin(list, startIdx):
    m = min(list[startIdx:])
    minIdx = list.index(m)
    swap(list, startIdx, minIdx)
    
	
list1 = [3,2,1,5]
startIdx = 1
print("original list:", list1)
bubbleMin(list1, 1)
print("after bubbleMin(list, startIdx =", startIdx, "):", list1)

list2 = [3,2,1,5]
startIdx = 0
print("original list:", list2)
bubbleMin(list2, 0)
print("after bubbleMin(list, startIdx =", startIdx, "):", list2)



