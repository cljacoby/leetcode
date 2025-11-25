// https://leetcode.com/problems/diagonal-traverse
struct Solution;

#[derive(Debug)]
enum Dir {
    UpRight,
    DownLeft,
}

impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        let n = mat.len();
        let m = mat[0].len();
        let mut arr = Vec::with_capacity(n * m);
        let mut dir = Dir::UpRight;
        let mut i = 0;
        let mut j = 0;

        loop {
            arr.push(mat[i][j]);
            println!("dir={:?}, i={}, j={}, arr={:?}", dir, i, j, arr);
            match (
                &dir,
                i >= 1,                   // up
                j + 1 < m,                // right
                i + 1 < n,                // down
                j >= 1,                   // left
                i == n - 1 && j == m - 1, // end
            ) {
                (_, _, _, _, _, true) => break,
                (Dir::UpRight, true, true, _, _, _) => {
                    j += 1;
                    i -= 1
                }
                (Dir::UpRight, false, true, _, _, _) => {
                    j += 1;
                    dir = Dir::DownLeft
                }
                (Dir::UpRight, false, false, true, _, _) => {
                    i += 1;
                    dir = Dir::DownLeft
                }
                (Dir::DownLeft, _, _, true, true, _) => {
                    j -= 1;
                    i += 1
                }
                (Dir::DownLeft, _, _, true, false, _) => {
                    i += 1;
                    dir = Dir::UpRight
                }
                (Dir::DownLeft, _, true, false, false, _) => {
                    j += 1;
                    dir = Dir::UpRight
                }
                (dir, up, rg, dw, lf, end) => {
                    panic!(
                        "bad move, dir={:?}, i={}, j={}, arr={:?}, up={}, rg={}, dw={}, lf={}, end={}",
                        dir, i, j, arr, up, rg, dw, lf, end
                    );
                }
            }
        }

        arr
    }
}

fn main() {
    let tests = vec![
        (
            vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]],
            vec![1, 2, 4, 7, 5, 3, 6, 8, 9],
        ),
        (
            vec![vec![1, 2, 3, 4, 5], vec![6, 7, 8, 9, 10]],
            vec![1, 2, 6, 7, 3, 4, 8, 9, 5, 10],
        ),
        (vec![vec![1, 2], vec![3, 4]], vec![1, 2, 3, 4]),
    ];


    for (mat, solution) in tests {
        let result = Solution::find_diagonal_order(mat);
        assert_eq!(result, solution);
    }
}
