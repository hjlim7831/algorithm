H, M = map(int, input().split())
sM = (M-45)%60
if M>=45:
    sH = H
else:
    sH = (H - 1)%24
print(sH, sM)