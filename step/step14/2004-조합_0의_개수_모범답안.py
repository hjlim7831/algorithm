n, m = map(int,input().split())

def count_number(n,k):
    count = 0
    while n != 0:
        n = n // k
        count += n
    return count

five_count = count_number(n,5) - count_number(m,5) - count_number(n-m,5)
two_count = count_number(n,2) - count_number(m,2) - count_number(n-m,2)

ans = min(five_count, two_count)
print(ans)

#이렇게 계산하면 팩토리얼에서 n의 개수를 계산하는 것이
#훨씬 빨라질 것 같다. (그 전의 방식에서는 모든 숫자마다 일일이 나눠봐야 배수임을 아는 방식이니까.)
#다시 풀기