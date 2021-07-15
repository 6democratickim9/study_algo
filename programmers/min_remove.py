def solution(arr):
    if len(arr)>1:
        arr.pop(arr.index(min(arr)))
        return arr
    else:
        return [-1]
    
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
# i가 mylist의 min보다 클 때 i를 return 
print(rm_small([10]))