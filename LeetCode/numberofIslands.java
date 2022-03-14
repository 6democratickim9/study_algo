class Solution {
    private int n;
    private int m;
    
    private void doDFS(char[][] grid, int startRow, int endRow){//Column
        if ( startRow < 0 || endRow < 0 || startRow >= n || endRow >= m || grid[startRow][endRow] !='1') return;
        grid[startRow][endRow] ='0';
        doDFS(grid,startRow+1,endRow);
        doDFS(grid,startRow-1,endRow);
        doDFS(grid,startRow,endRow-1);
        doDFS(grid,startRow,endRow+1);
        
    }
    public int numIslands(char[][] grid) {
        int count=0;
        n = grid.length;
        if(n==0) return 0;
        m = grid[0].length;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j] == '1'){
                    doDFS(grid, i, j);
                    ++count;
            }

            }
        }
        return count;
    }
    
}
