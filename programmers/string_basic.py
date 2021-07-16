# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)
#     # isdigit()이라는 함수를 사용해 s가 정수로 되어있는지 판별하고 True 임과 동시에 len(s)가 4나 6안에 있는지 판별 후 return

def solution(s):
    try:
        if len(s)==4 or len(s)==6:
            return bool(int(s))
        else: return False
    except:
        return False
