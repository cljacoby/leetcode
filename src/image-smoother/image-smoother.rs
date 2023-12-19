// https://leetcode.com/problems/image-smoother

struct Solution;

impl Solution {
    pub fn smooth_avg(img: &Vec<Vec<i32>>, rows: usize, cols: usize, i: usize, j: usize) -> i32 {
        assert!(i < rows && j < cols);

        let xmin = i.checked_sub(1).unwrap_or(0);
        let xmax = if i + 1 < rows { i + 1 } else { i };
        let ymin = j.checked_sub(1).unwrap_or(0);
        let ymax = if j + 1 < cols { j + 1 } else { j };
        let mut tot = 0;
        let mut count = 0;

        for x in xmin..=xmax {
            for y in ymin..=ymax {
                tot += img[x][y];
                count += 1;
            }
        }

        tot as i32 / count as i32
    }

    pub fn image_smoother(img: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let rows = img.len();
        let cols = img[0].len();
        let mut out = vec![vec![0 ; cols] ; rows];

        for i in 0..rows {
            for j in 0..cols {
                out[i][j] = Solution::smooth_avg(&img, rows, cols, i, j);
            }
        }

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![vec![1,1,1], vec![1,0,1], vec![1,1,1]],
            vec![vec![0,0,0], vec![0,0,0], vec![0,0,0]],
        ),
        (
            vec![vec![100,200,100],vec![200,50,200],vec![100,200,100]],
            vec![vec![137,141,137],vec![141,138,141],vec![137,141,137]],
        )
    ];


    for (img, solution) in tests {
        let result = Solution::image_smoother(img);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}

