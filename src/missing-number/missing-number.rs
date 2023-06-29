// https://leetcode.com/problems/missing-number
struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let s: HashSet<i32> = nums.into_iter().collect();

        for i in 0..=(s.len() as i32) {
            if !s.contains(&i) {
                return i;
            }
        }

        panic!("Did not find solution")
    }
}

fn main() {
    let tests = vec![
        (vec![9,6,4,2,3,5,7,0,1], 8),
        (vec![0,1], 2),
        (vec![3,0,1], 2),
    ];

    for (nums, solution) in tests {
        let result = Solution::missing_number(nums);
        assert_eq!(result, solution);
    }
}
