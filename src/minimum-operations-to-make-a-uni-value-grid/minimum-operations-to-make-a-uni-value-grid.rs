// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid
struct Solution;

impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let mut prev: Option<i32> = None;
        let mut vals: Vec<i32> = grid.into_iter().flatten().collect();

        for val in vals.iter() {
            let rem = val % x;
            if let Some(prev) = prev {
                if rem != prev {
                    return -1;
                }
            } else {
                prev = Some(rem);
            }
        }

        vals.sort();
        let med = vals[vals.len() / 2];
        let mut ops = 0;
        for val in vals.iter() {
            ops += i32::abs(med - val) / x;
        }

        ops
    }
}

fn main() {
    let tests = vec![
        (vec![vec![2,4],vec![6,8]], 2, 4),
        (vec![vec![1,5],vec![2,3]], 1, 5),
        (vec![vec![529,529,989],vec![989,529,345],vec![989,805,69]], 92, 25),
    ];

    for (grid, x, solution) in tests {
        let result = Solution::min_operations(grid, x);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
