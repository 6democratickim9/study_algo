burger = []
soda = []
for _ in range(0,3):
    num = int(input())
    burger.append(num)
for _ in range(0,2):
    num = int(input())
    soda.append(num)
print((min(burger)+min(soda))-50)
