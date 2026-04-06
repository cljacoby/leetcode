// https://leetcode.com/problems/rotting-oranges
struct Solution;

use tracing::{info};

use std::collections::{HashSet, VecDeque};

#[derive(Debug)]
enum Cell {
    Fresh,
    Rotten,
    Empty,
}

impl From<i32> for Cell {
    fn from(x: i32) -> Cell {
        match x {
            0 => Cell::Empty,
            1 => Cell::Fresh,
            2 => Cell::Rotten,
            _ => panic!("invalid cell value"),
        }
    }
}

impl Solution {
    const DIRS: [(isize, isize); 4]= [
        (0, -1),
        (0, 1),
        (1, 0),
        (-1, 0),
    ];

    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let cells = rows * cols;

        let mut grid: Vec<Vec<Cell>> = grid
            .into_iter()
            .map(|row| row.into_iter().map(|x| Cell::from(x)).collect())
            .collect();

        let mut fresh: HashSet<(usize, usize)> = HashSet::with_capacity(cells);
        let mut q: VecDeque<(usize, usize)> = VecDeque::with_capacity(cells);
        let mut r: VecDeque<(usize, usize)> = VecDeque::with_capacity(cells);
        let mut ticks = 0;

        for (i, row) in grid.iter().enumerate() {
            for (j, cell) in row.iter().enumerate() {
                match cell {
                    Cell::Empty => {},
                    Cell::Fresh => {
                        fresh.insert((i, j));
                    },
                    Cell::Rotten => {
                        r.push_back((i, j));
                    },
                };
            }
        }
        
        info!(fresh=?fresh, q=?q, r=?r, "initial state");

        while r.len() > 0 || q.len() > 0 {
            info!(q=?q, r=?r, fresh=?fresh, grid=?grid, "loop start");
            if fresh.len() == 0 {
                break
            }
            while let Some(coord) = r.pop_front() {
                q.push_back(coord)
            }
            while let Some((i, j)) = q.pop_front() {
                debug_assert!(i < rows && j < cols, "index out of bounds");
                debug_assert!(matches!(grid[i][j], Cell::Rotten), "dequed non-rotten cell");
                for (dx, dy) in Self::DIRS.iter() {
                    let x = (i as isize) + dx;
                    let y = (j as isize) + dy;
                    if x >= 0 && x < (rows as isize) && y >= 0 && (y < cols as isize) {
                        let x = x as usize;
                        let y = y as usize;
                        if matches!(grid[x][y], Cell::Fresh) {
                            grid[x][y] = Cell::Rotten;
                            let rotted = (x, y);
                            fresh.remove(&rotted);
                            r.push_back(rotted);
                        }
                    }
                }
            }
            ticks += 1;
        }

        if fresh.is_empty() {
            ticks
        } else {
            -1
        }
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (vec![vec![2, 1, 1], vec![1, 1, 0], vec![0, 1, 1]], 4),
        (vec![vec![0, 2]], 0),
    ];

    for (grid, solution) in tests {
        let result = Solution::oranges_rotting(grid);
        assert_eq!(result, solution);
    }
}
