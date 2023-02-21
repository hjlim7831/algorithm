N = int(input())
numl = [0 for i in range(N)]
for i in range(N):
    numl[i] = int(input())
numl.sort()
print("\n".join(map(str,numl)))