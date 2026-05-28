// https://leetcode.com/problems/max-area-of-island
struct Solution;

use std::collections::VecDeque;

impl Solution {
    fn walk_island(
        q: &mut VecDeque<(usize, usize)>,
        grid: &Vec<Vec<i32>>,
        rows: usize,
        cols: usize,
        visited: &mut Vec<Vec<bool>>,
    ) -> i32 {
        let mut area = 0;

        while let Some((x, y)) = q.pop_front() {
            if visited[x][y] {
                continue
            }
            if grid[x][y] != 1 {
                continue
            } 

            visited[x][y] = true;
            area += 1;

            if let Some(dx) = x.checked_sub(1) {
                q.push_back((dx, y));
            }
            if let Some(dy) = y.checked_sub(1) {
                q.push_back((x, dy));
            }
            if let Some(dx) = x.checked_add(1) && dx < rows {
                q.push_back((dx, y));
            }
            if let Some(dy) = y.checked_add(1) && dy < cols {
                q.push_back((x, dy));
            }
        }

        area
    }

    pub fn max_area_of_island(grid: Vec<Vec<i32>>) -> i32 {
        let mut max = 0;
        let rows = grid.len();
        let cols = grid.get(0).map(|row| row.len()).unwrap_or(0);
        let mut visited = vec![vec![false; cols]; rows];
        let mut q: VecDeque<(usize, usize)> = VecDeque::with_capacity(rows * cols);

        for (i, row) in grid.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                if *val == 1 {
                    q.push_back((i, j));
                    let area = Self::walk_island(&mut q, &grid, rows, cols, &mut visited);
                    max = i32::max(area, max);
                }
            }
        }


        max
    }
}

fn main() {
    let tests = vec![
        (vec![
            vec![0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            vec![0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            vec![0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            vec![0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ], 6),
        (
            vec![vec![0,0,0,0,0,0,0,0]],
            0,
        )
    ];

    for (grid, solution) in tests {
        let result = Solution::max_area_of_island(grid);
        assert_eq!(result, solution);
    }

}
