// https://leetcode.com/problems/pascals-triangle
struct Solution;

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let n = num_rows as usize;
        let mut triangle: Vec<Vec<i32>> = Vec::with_capacity(n);

        for i in 0..n {
            let mut row = Vec::with_capacity(i + 1);
            row.push(1);

            if i > 0 {
                for j in 0..(i - 1) {
                    let x = triangle[i - 1][j] + triangle[i - 1][j + 1];
                    row.push(x);
                }
                row.push(1);
            }

            triangle.push(row);
        }

        triangle
    }
}

fn main() {
    let tests = vec![
        (
            5,
            vec![
                vec![1],
                vec![1, 1],
                vec![1, 2, 1],
                vec![1, 3, 3, 1],
                vec![1, 4, 6, 4, 1],
            ],
        ),
        (1, vec![vec![1]]),
    ];

    for (num_rows, solution) in tests {
        let result = Solution::generate(num_rows);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
