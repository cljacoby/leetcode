struct Solution;

impl Solution {

    /// Note: This functions assumes the matrix rows are all equal length,
    /// Which is required for a valid matrix.
    pub fn dimensions(matrix: &Vec<Vec<i32>>) -> (i32, i32) {
        (matrix.len() as i32, matrix.get(0).unwrap().len() as i32)
    }

    pub fn matrix_reshape(nums: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        let (x, y) = Solution::dimensions(&nums);
        if x * y != r * c {
            return nums;
        }

        let mut matrix: Vec<Vec<i32>> = vec![Vec::with_capacity(c as usize); r as usize];
        let mut row_idx = 0;
        let mut col_idx = 0;

        for (i, row) in nums.iter().enumerate() {
            for (j, el) in row.iter().enumerate() {
                matrix[row_idx].push(*el);
                col_idx += 1;
                if col_idx % c == 0 {
                    row_idx += 1;
                }
            }
        }

        println!("matrix = {:?}", matrix);
        matrix
    }
}

fn main() {
    println!("compiled without cargo");
    let matrix = vec![
        vec![1, 2],
        vec![3, 4],
    ];
    let result = Solution::matrix_reshape(matrix, 1, 4);
    println!("result = {:?}", result);
}
