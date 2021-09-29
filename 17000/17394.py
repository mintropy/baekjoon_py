"""
Title : 핑거 스냅
Link : https://www.acmicpc.net/problem/17394
"""

import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())

is_prime = [True] * 100_001
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, 100_001):
    if is_prime[i]:
        primes.append(i)
        for j in range(2 * i, 100_001, i):
            is_prime[j] = False


for _ in range(int(input())):
    n, a, b = MIIS()
    # a와 b사이 소수
    prob_primes = []
    for p in primes:
        if a <= p <= b:
            prob_primes.append(p)
        elif p > b:
            break
    
    # a, b 사이 소수가 없는 경우
    if not prob_primes:
        print(-1)
        continue
    # a보다 작으면 생명체를 늘리는 핑거스넵
    elif n <= a:
        print(prob_primes[0] - n)
        continue
    
    min_finger_snap = n
    queue = collections.deque([(n, 0)])
    # 최소 핑거 스냅 횟수로
    visited = [n] * (1_000_000 + 1)
    while queue:
        m, finger_sanp = queue.popleft()
        if finger_sanp >= min_finger_snap:
            break
        # 이미 확인한 생명체 수 인경우
        if finger_sanp > visited[m]:
            continue
        else:
            if m in prob_primes and finger_sanp < min_finger_snap:
                min_finger_snap = finger_sanp
            visited[m] = finger_sanp
        # 생명체 수가 a보다 작으면, 값 비교 후 continue
        if m < a:
            if min_finger_snap < finger_sanp + (prob_primes[0] - m):
                min_finger_snap = finger_sanp + (prob_primes[0] - m)
            continue
        else:
            if visited[m // 2] > finger_sanp + 1:
                queue.append((m // 2, finger_sanp + 1))
            if visited[m // 3] > finger_sanp + 1:
                queue.append((m // 3, finger_sanp + 1))
            if m + 1 < 1_000_001 and visited[m + 1] > finger_sanp + 1:
                queue.append((m + 1, finger_sanp + 1))
            if m > 0 and visited[m - 1] > finger_sanp + 1:
                queue.append((m - 1, finger_sanp + 1))
    print(min_finger_snap)

'''
Counter Example
1
1000000 29 29

'''
