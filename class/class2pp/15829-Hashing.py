def Hash(a):
    r = 31
    M = 1234567891
    ans = 0
    for i in range(len(a)):
        a_num = int(ord(a[i]))-96
#        print(a_num)
        ans += a_num*r**i
    return ans%M

L = int(input())
string = input()
print(Hash(string))