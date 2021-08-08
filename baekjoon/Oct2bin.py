import sys
A=(sys.stdin.readline())
print((bin(int('0o'+A,8)))[2:])