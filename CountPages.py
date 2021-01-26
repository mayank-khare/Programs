def countPage(n,p):
    return min(p//2,n//2 - p//2)

n = int(input().strip())
p = int(input().strip())
result = countPage(n,p)
print (result)