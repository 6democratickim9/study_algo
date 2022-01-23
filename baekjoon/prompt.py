N=int(input())
file = input()
for _ in range(0,N-1):
    tmp = input()
    try:
        if tmp is not file:
            for idx in range(len(file)):
                if(tmp[idx]!=file[idx]):
                    file = file[:idx]+"?"+file[idx+1:]
    except: continue

print(file)