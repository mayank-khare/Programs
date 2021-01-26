def climbing(scores, alice):
    unique_score=list(reversed(sorted(set(scores))))

    i=len(alice)-1
    j = 0
    ans = []

    while i>=0:
        if j >= len(unique_score) or unique_score[j] <= alice[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1
    return reversed(ans)

n = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
result=climbing(scores, alice)
print (*result)