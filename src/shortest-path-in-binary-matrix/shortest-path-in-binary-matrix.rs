// https://leetcode.com/problems/shortest-path-in-binary-matrix

/**
 * Seems the optimal solutions are using a similar algorithm,
 * except instead of using just a VecDeque and BFS, their using
 * a BinaryHeap, and the A* algorithm with a heuristic to reduce
 * the overall number of cells which need to be visited.
 *
 * Should try to implement one of those solutions for learning purposes.
 * */

struct Solution;

use std::collections::HashSet;
use std::collections::VecDeque;

impl Solution {
    const DIRS: [(isize, isize); 8] = [
        (-1, -1), // up-left
        (-1, 1),  // up-right
        (1, -1),  // down-left
        (1, 1),   // down-right
        (1, 0),   // down
        (-1, 0),  // up
        (0, 1),   // right
        (0, -1),  // left
    ];

    pub fn shortest_path_binary_matrix(grid: Vec<Vec<i32>>) -> i32 {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut visited = HashSet::with_capacity(rows * cols);
        let mut q: VecDeque<((usize, usize), i32)> = VecDeque::with_capacity(rows * cols);
        let mut mx: i32 = i32::MAX;
        if grid[0][0] == 0 {
            q.push_back(((0, 0), 1));
        }

        while let Some(((x, y), path)) = q.pop_front() {
            if x == rows - 1 && y == cols - 1 {
                mx = i32::min(mx, path);
                continue;
            }
            for (dx, dy) in Self::DIRS.iter() {
                let i = match x.checked_add_signed(*dx) {
                    Some(i) => i,
                    None => continue,
                };
                let j = match y.checked_add_signed(*dy) {
                    Some(j) => j,
                    None => continue,
                };
                if i >= rows || j >= cols || grid[i][j] != 0 || visited.contains(&(i, j)) {
                    continue;
                }
                q.push_back(((i, j), path + 1));
                visited.insert((i, j));
            }
        }

        if mx == i32::MAX {
            -1
        } else {
            mx
        }
    }
}

fn main() {
    let tests = vec![
        (vec![vec![0, 1], vec![1, 0]], 2),
        (vec![vec![0, 0, 0], vec![1, 1, 0], vec![1, 1, 0]], 4),
        (vec![vec![1, 0, 0], vec![1, 1, 0], vec![1, 1, 0]], -1),
    ];

    for (grid, solution) in tests.into_iter() {
        let result = Solution::shortest_path_binary_matrix(grid);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
