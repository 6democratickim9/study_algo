from collections import deque

def solution(maps):
    # 맵의 크기
    n, m = len(maps), len(maps[0])
    
    # 이동할 네 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS 실행
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        # 상대 팀 진영에 도착하면 현재까지의 이동 칸 수 반환
        if x == n - 1 and y == m - 1:
            return maps[x][y]
        
        # 상하좌우로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵 범위 안에 있고, 이동할 수 있는 칸일 때
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이동하면서 거리 기록, 이전 거리 + 1
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    # 상대 팀 진영에 도달할 수 없으면 -1 반환
    return -1
