import sys
input = sys.stdin.readline

n = int(input())
# 동기의 수 n명을 받는다
m = int(input())
# 루프에 들어갈 리스트의 길이 m이 주어진다.
res = dict()
resSet = set()
# 연결된 그래프를 만들기 위해서는 res라는 딕셔너리를 만들어준다
#  set을 사용하여 중복된 값이 없는 set을 만들어준다.
for _ in range(m):
    key, item = map(int, input().split())
    # key와 item 으로 나누어 인접된 노드를 받는다
    if key not in res:
        res[key] = list()
    # 키가 res 에 없다면 키:[] 형태로 값을 저장한다.(처음으로 저장되는 값)
    if item not in res:
    # item이 res에 없다면 res에 item:[]형태로 저장한다.
        res[item] = list()
    res[key].append(item)
    # 키:[]의 []안에 item 값을 넣어주고, 아이템:[]부분에는 key값을 넣어준다.
    res[item].append(key)
# 그래프의 모양을 완성
# 그래프에서 1에서 닿을 수 있는 노드들만 가져오는 식
for key in res[1]:
    resSet.add(key)
    # resSet에 []안에 있는 값을 삽입한다.
    if key not in res:
        continue
    else:
        for item in res[key]:
            # res 안에 있는 키값의 value를 resSet에 넣는다(인접 노드를 넣어줌)중복값은set에 포함되지 않으니 중복되면 알아서 저장되지 않음.
            resSet.add(item)

print(len(resSet) - 1)
# 1과 인접한 노드들이 resSet에 모이면(1도 포함되기 때문에)1을 빼고 값을 출력한다.
# 친구의친구의친구는 안되고 친구의친구까지만..!
# 다른 사람의 답안

# 예시:1-3