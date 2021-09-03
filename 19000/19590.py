"""
Title : 비드맨
Link : https://www.acmicpc.net/problem/19590
"""

import sys
input = sys.stdin.readline


n = int(input())
beads = sorted([int(input()) for _ in range(n)])

# 없어지지 않은 시작점
st = 0
# 지금 보고 있는 왼쪽 / 오른쪽
left, right = 0, n - 1

# 지금 보고 있는 외쪽의 구슬 개수
left_count = beads[0]
# 마지막에는 한 종류만 남게 됨
while st < n:
    if left == right:
        break
    # 가장 오른쪽이 1개가 되면, 가능한 모두 제거, 종료
    if right == n - 1 and beads[-1] == 1:
        pass
    # 아닐 때,
    # r_now 기준으로 확인하며 진행
    # 1. 왼쪽이 l_now이면 하나씩 부딪히고 가장 오른쪽으로 이동
    # 2. 왼쪽과 개수가 같다면 하나 부딪히고 왼쪽으로 이동
    # 3. 왼쪽과 개수의 차이가 둘 이상이면 같아질때까지 부딪히고 가장 오른쪽으로 이동
    else:
        if right - left == 1:
            pass
        elif beads[right] == beads[right -1] + 1:
            pass
        else:
            pass
    pass


'''
Counter Example
8
2
2
2
3
3
3
5
6
ans : 0

'''