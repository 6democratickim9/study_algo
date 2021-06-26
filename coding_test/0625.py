## 소수판별기

# def isPrime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return False
#     return True

# a = [12,13,7,9,19]
# for y in a:
#     if isPrime(y):
#         print(y,end= ' ')

### 람다함수
#sort 라는 것의 인자로 람다함수를 자주 사용함
a = [1,2,3]

plus_two=lambda x:x+2
def plus_one(x):
    return x+1

print(list(map(lambda x: x+1,a))) # plus_one 과 같은 자료