struct Solution {}

impl Solution {
   
    pub fn area(row: usize, col: usize, grid: &Vec<Vec<i32>>, seen: &mut Vec<Vec<bool>>) -> i32 {
        // Check coordinate in grid
        // Check grid doesn't equal 0
        // Checl not already seen cooordinate
        if row < 0
            || col < 0
            || row >= grid.len()
            || col >= grid[0].len()
            || grid[row][col] == 0
            || seen[row][col]
        {
            return 0;
        }

        // This is valid coordinate. Add to seen coordinates for future recursions.
        seen[row][col] = true;

        // Both `row` and `col` are type usize. Producing a negative value for usize is a
        // bounds overflow for the type. Therefore, check the value before executing
        // leftward and downward board motion to prevent overflow.
        let mut area = 1;
        area += Solution::area(row, col + 1, grid, seen);
        area += Solution::area(row + 1, col, grid, seen);
        if col > 0 {
            area += Solution::area(row, col - 1, grid, seen);
        }
        if row > 0 {
            area += Solution::area(row - 1, col, grid, seen);
        }

        area
    }

    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut seen = vec![vec![false; cols]; rows];
        let mut area = 0;

        for i in 0..rows {
            for j in 0..cols {
                area = std::cmp::max(area, Solution::area(i, j, &grid, &mut seen));
            }
        }

        area
    }
}

fn main() {
    // let grid: Vec<Vec<i32>> = vec![
    //     vec![0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    //     vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    //     vec![0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    //     vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    //     vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    //     vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    //     vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    //     vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    // ];

    let grid: Vec<Vec<i32>> = vec![
        vec![0, 1,],
        vec![1, 1,],
    ];
    
    let area = Solution::max_area_of_island(grid);
    println!("area = {:?}", area);

}
