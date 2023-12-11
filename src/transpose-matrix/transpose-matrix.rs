// https://leetcode.com/problems/transpose-matrix
struct Solution;

impl Solution {
    pub fn transpose(matrix: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut out: Vec<Vec<i32>> = vec![vec![i32::MIN; rows]; cols];

        for i in 0..rows {
            for j in 0..cols {
                out[j][i] = matrix[i][j];
            }
        }

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]],
            vec![vec![1, 4, 7], vec![2, 5, 8], vec![3, 6, 9]],
        ),
        (
            vec![vec![1, 2, 3], vec![4, 5, 6]],
            vec![vec![1, 4], vec![2, 5], vec![3, 6]],
        ),
    ];

    for (input, solution) in tests {
        let result = Solution::transpose(input);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
