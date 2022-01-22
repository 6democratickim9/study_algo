for idx in range(0,3):
    N=int(input())
    nums = [int(input()) for i in range(0,N)]
    print(((str)(sum(nums)))[0] if sum(nums)<=0 else '+')
