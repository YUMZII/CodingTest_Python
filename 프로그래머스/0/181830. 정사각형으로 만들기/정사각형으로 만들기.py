def solution(arr):
    r=len(arr)
    c=len(arr[0])
    
    n=max(r,c)
    
    if c<n:
        for i in range(r):
            arr[i] += [0] * (n-c)
    if r<n:
        for j in range(n-r):
            arr.append([0]*n)
    return arr