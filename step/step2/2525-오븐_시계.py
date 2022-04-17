A, B = map(int, input().split())
C = int(input())
end_tm = A*60+B+C
end_hour = (end_tm//60)%24
end_minute = end_tm%60
print(end_hour, end_minute)