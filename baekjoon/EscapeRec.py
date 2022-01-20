rec = list(map(int,input().split()))
rec.append(rec[2]-rec[0])
rec.append(rec[3]-rec[1])
print(min(rec))
