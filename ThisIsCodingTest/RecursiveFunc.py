# 재귀함수란 자기 자신을 다시 호출하는 함수
# 스택과 유사한 구조를 가지고 있다
# 스택이 필요할 때 그냥 재귀함수를 구현해 사용하는 경우도 있음

# def recursive_function():
#     print('재귀함수를 호출합니다')
#     recursive_function()
    # 자기자신을 다시 호출함
    # 실행하면 무한히 발생하다가 maximum recurstion depth exceed라는 오류메세지가 뜸
    # 재귀 깊이를 더 늘려주거나 내부적으로 stack라이브러리를 사용하는 방식으로 매핑시켜줄 수 있음
    # 파이썬에는 깊이제한이 있기때문에 미리 정해주어야 함
    # 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음

def recursive_function(i):
    if i ==100:
        return
    print(i,"번째 재귀함수에서",i+1,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀함수를 종료합니다.")
recursive_function(1)
# 100번까지 호출되었다가 99번까지 달성하면 다시 1로 돌아가며 종료됨