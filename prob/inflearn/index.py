
msg = "Adventure Time!"
print(msg.upper())
print(msg.lower())
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[:2])
print(len(msg))
for i in range(len(msg)):
    print(msg[i],end =' ')
print('\n')
for x in msg:
    if x.isupper(): #대문자면 참이 된다
        print(x,end=' ')
print('\n')
for x in msg:
    if x.islower(): #소문자면 참이 된다
        print(x,end=' ')
print('\n')
for x in msg:
    if x.isalpha(): #알파벳일떄 참이 된다
        print(x,end=' ')

print('\n')

tmp = 'AZ'
for x in tmp:
    print(ord(x))#아스키넘버 출력-> 대문자 A의 아스키넘버, 대문자 Z의 아스키넘버

tmp = 'az'
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp)) #아스키넘버에 대응되는 숫자 출력

