// https://leetcode.com/problems/number-of-islands
struct Solution;

use std::collections::VecDeque;

type Coord = (usize, usize);

impl Solution {

    #[tracing::instrument(ret)]
    pub fn walk_island(
        grid: &Vec<Vec<char>>,
        rows: usize,
        cols: usize,
        q: &mut VecDeque<Coord>,
        visited: &mut Vec<Vec<bool>>
    ) {
        while let Some((x, y)) = q.pop_front() {
            let val = grid.get(x)
                .expect("failed to index rows")
                .get(y)
                .expect("failed to index cols");
            if *val != '1' || visited[x][y] {
                continue
            }
            visited[x][y] = true;
            if let Some(dx) = x.checked_sub(1) {
                q.push_back((dx, y));
            }
            if let Some(dx) = x.checked_add(1) && dx < rows {
                q.push_back((dx, y));
            }
            if let Some(dy) = y.checked_sub(1) {
                q.push_back((x, dy));
            }
            if let Some(dy) = y.checked_add(1) && dy < cols {
                q.push_back((x, dy));
            }
        }
    }

    #[tracing::instrument(ret)]
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let rows = grid.len();
        let cols = grid.get(0)
            .expect("grid is empty").len();
        let mut count = 0;
        let mut visited = vec![vec![false; cols]; rows];
        let mut q = VecDeque::with_capacity(rows * cols);

        for (i, row) in grid.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                if *val == '1' && !visited[i][j] {
                    q.push_back((i, j));
                    Self::walk_island(&grid, rows, cols, &mut q, &mut visited);
                    count += 1;
                } 
            }
        }

        count
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![
                vec!['1','1','1','1','0'],
                vec!['1','1','0','1','0'],
                vec!['1','1','0','0','0'],
                vec!['0','0','0','0','0']
            ],
            1,
        ),
        (
            vec![
                vec!['1','1','0','0','0'],
                vec!['1','1','0','0','0'],
                vec!['0','0','1','0','0'],
                vec!['0','0','0','1','1']
            ],
            3
        )
    ];

    for (grid, solution) in tests {
        let result = Solution::num_islands(grid);
        assert_eq!(result, solution);
    }
}
