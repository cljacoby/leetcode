pub struct Solution;

pub type Grid=Vec<Vec<i32>>;

// OrangeState could ideally be an enum, but leetcode's problem input
// uses a i32 representation.
pub type OrangeState=i32;

const EMPTY: i32 = 0;
const FRESH: i32 = 1;
const ROTTEN: i32 = 2;

impl Solution {

    pub fn print_grid(grid: &Grid) {
        println!("[");
        for row in grid.iter() {
            println!("{:?},", row);
        }
        println!("]");
    }
    
    pub fn none(grid: &Grid, state: OrangeState) -> bool {
        !Solution::any(grid, state)
    }

    pub fn all(grid: &Grid, state: OrangeState) -> bool {
        grid.iter()
            .flatten()
            .map(|orange| *orange == state)
            .fold(true, |acc, b| acc && b)
    }

    pub fn any(grid: &Grid, state: OrangeState) -> bool {
        grid.iter()
            .flatten()
            .map(|orange| *orange == state)
            .fold(false, |acc, b| acc || b)
    }

    pub fn is_valid_state(state: i32) -> bool {
        state ==  EMPTY || state == FRESH || state == ROTTEN
    }

    pub fn indices_of(grid: &Grid, state: i32) -> Vec<(usize, usize)> {
        if !Solution::is_valid_state(state) {
            panic!("Can only retrieve indices for EMPTY(0), FRESH(1), or ROTTEN(2)");
        }

        let mut indices: Vec<(usize, usize)> = Vec::new();
        for (i, row) in grid.iter().enumerate() {
            for (j, orange) in row.iter().enumerate() {
                if *orange == state {
                    indices.push((i, j));
                }
            }
        }

        indices
    }

    pub fn tick(mut grid: Grid) -> Grid {
        let row_len = grid.len();
        let col_len = grid[0].len(); // assuming constant row width

        let rottens = Solution::indices_of(&grid, ROTTEN);
        for (x, y) in rottens.iter() {
            // left
            if *y > 0 && grid[*x][*y - 1] == FRESH {
                grid[*x][*y - 1] = 2;
            }
            // right
            if *y < col_len - 1 && grid[*x][*y + 1] == FRESH {
                grid[*x][*y + 1] = 2;
            }
            // up
            if *x > 0 && grid[*x - 1][*y] == FRESH {
                grid[*x - 1][*y] = 2;
            }
            // down
            if *x < row_len - 1 && grid[*x + 1][*y] == FRESH {
                grid[*x + 1][*y] = 2;
            }
        }

        grid
    }


    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        let mut ticks = 0;
        let last_grid = grid.clone();
        while Solution::any(&grid, FRESH) {
            let last_grid = grid.clone();
            grid = Solution::tick(grid);
            ticks += 1;
            if grid == last_grid {
                return -1;
            }
        }
    
        ticks
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_any() {
        let no_fresh_grid = vec![
            vec![2,2,2],
            vec![0,0,0],
            vec![0,2,2]
        ];
        let some_fresh_grid = vec![
            vec![2,2,2],
            vec![0,1,0],
            vec![0,2,2]
        ];

        assert_eq!(false, Solution::any(&no_fresh_grid, FRESH));
        assert_eq!(true, Solution::any(&some_fresh_grid, FRESH));
    }

    #[test]
    fn test_1() {
        let grid = vec![
            vec![2,1,1],
            vec![1,1,0],
            vec![0,1,1]
        ];
        let solution = 4;
        assert_eq!(solution, Solution::oranges_rotting(grid));
    }

    #[test]
    fn test_2() {
        let grid = vec![
            vec![2,1,1],
            vec![0,1,1],
            vec![1,0,1]
        ];
        let solution = -1;
        assert_eq!(solution, Solution::oranges_rotting(grid));
    }


    #[test]
    fn test_3() {
        let grid = vec![
            vec![0,2],
        ];
        let solution = 0;
        assert_eq!(solution, Solution::oranges_rotting(grid));
    }

    #[test]
    fn test_4() {
        let grid = vec![
            vec![1,1,1,1],
        ];
        let solution = -1;
        assert_eq!(solution, Solution::oranges_rotting(grid));
    }

    #[test]
    fn test_5() {
        let grid = vec![
            vec![0,0,0,1,1],
        ];
        let solution = -1;
        assert_eq!(solution, Solution::oranges_rotting(grid));
    }

    #[test]
    fn test_6() {
        let grid = vec![
            vec![2],
            vec![2],
            vec![1],
            vec![0],
            vec![1],
            vec![1],
        ];
        let solution = -1;
        assert_eq!(solution, Solution::oranges_rotting(grid));
    }

}
