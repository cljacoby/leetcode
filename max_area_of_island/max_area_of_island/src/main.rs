struct Solution {}

impl Solution {
    pub fn neighbors(coord: (usize, usize), grid: &Vec<Vec<i32>>) -> Vec<(usize, usize)> {
        let (x, y) = coord;
        let mut neighbors = Vec::with_capacity(4);

        // can go up?
        if y > 0 {
            neighbors.push((x, y - 1));
        }
        // can go right?
        if x < grid[0].len() - 1 {
            neighbors.push((x + 1, y));
        }
        // can go down?
        if y < grid.len() - 1 {
            neighbors.push((x, y + 1));
        }
        // can go left?
        if x > 0 {
            neighbors.push((x - 1, y));
        }

        neighbors
    }

    pub fn max_island(coord: (usize, usize), grid: &Vec<Vec<i32>>, area: i32) {
        let n_coords: Vec<(usize, usize)> = Solution::neighbors(coord, grid)
            .into_iter()
            .filter(|(x, y)| grid[*x][*y] == 1)
            .filter(|(x, y)| !(*x == coord.0 && *y == coord.1))
            .collect();

        println!("n_coords = {:?}", n_coords);
        for n_coord in n_coords {
            println!(
                "coord = {:?}, area = {:?}, n_coord = {:?}",
                coord, area, n_coord
            );
            Solution::max_island(n_coord, grid, area + 1);
        }
    }

    pub fn _max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        for (i, row) in grid.iter().enumerate() {
            for (j, el) in row.iter().enumerate() {
                let neighbors = Solution::neighbors((i, j), &grid);
                Solution::max_island((i, j), &grid, 1);
            }
        }

        0
    }

    pub fn area(row: usize, col: usize, grid: &Vec<Vec<i32>>, seen: &mut Vec<Vec<bool>>) -> i32 {
        println!("row = {:?}, col = {:?}", row, col);
        if (row < 0
            || row > grid.len()
            || col < 0
            || col > grid[0].len()
            || seen[row][col]
            || grid[row][col] == 0)
        {
            return 0;
        }

        seen[row][col] == true;

        Solution::area(row + 1, col, grid, seen)
            + Solution::area(row - 1, col, grid, seen)
            + Solution::area(row, col + 1, grid, seen)
            + Solution::area(row, col - 1, grid, seen)
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
    let grid: Vec<Vec<i32>> = vec![
        vec![0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        vec![0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ];

    let area = Solution::max_area_of_island(grid);
    println!("area = {:?}", area);

}
