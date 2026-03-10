// https://leetcode.com/problems/minimum-path-sum
struct Solution;

impl Solution {
    pub fn min_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let m = grid.first()
            .expect("grid has zero rows")
            .len();
        let mut dp = vec![vec![0; m]; n];

        for (i, row) in grid.iter().enumerate() {
            for (j, val) in row.iter().enumerate() {
                match (i > 0, j > 0) {
                    (false, false)  => dp[i][j] = *val,
                    (true,  false)  => dp[i][j] = val + dp[i-1][j],
                    (false, true)   => dp[i][j] = val + dp[i][j-1],
                    (true,  true)   => dp[i][j] = val + i32::min(dp[i-1][j], dp[i][j-1]),
                }
            }
        }

        dp[n-1][m-1]
    }
}

fn main() {
    let tests = vec![
        (
            vec![vec![1,3,1],vec![1,5,1],vec![4,2,1]],
            7,
        ),
        (
            vec![vec![1,2,3],vec![4,5,6]],
            12,
        ),
    ];

    for (grid, solution) in tests {
        let result = Solution::min_path_sum(grid);
        assert_eq!(result, solution);
    }
}
