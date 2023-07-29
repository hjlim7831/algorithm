def solution(n):
    A = [0] * (n + 5)
    A[0], A[1], A[2] = 1, 3, 10
    A[3], A[4], A[5] = 23, 62, 170
    for i in range(6, n):
        A[i] = (A[i-1] + 2 * A[i-2] + 6 * A[i-3] + A[i-4] - A[i-6]) % 1_000_000_007
    return A[n-1]