result = []
for t in range(int(input())) :
    result.append(f"#{t+1}")
    L = [1]
    for n in range(int(input())) :
        result.append(" ".join(list(map(str,L))))
        L1 = [0] + L
        for i in range(len(L)) :
            L1[i] += L[i]
        L = L1
print("\n".join(result))
