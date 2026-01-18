def solution(n):
    arr = [[0] * n for i in range(n)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    
    r,c = 0,0
    for num in range(1, n*n + 1):
        arr[r][c] = num
        nr = r+dr[d]
        nc = c+dc[d]
        
        if not(0 <= nr < n and 0 <= nc < n) or arr[nr][nc] != 0:
            d = (d + 1) % 4
            nr = r + dr[d]
            nc = c +dc[d]
        r,c = nr, nc
    return arr