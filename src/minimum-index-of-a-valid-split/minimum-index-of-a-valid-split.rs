// https://leetcode.com/problems/minimum-index-of-a-valid-split
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let mut rc: HashMap<&i32, usize> = HashMap::with_capacity(nums.len());
        let mut lc: HashMap<&i32, usize> = HashMap::with_capacity(nums.len());

        for num in nums.iter() {
            rc.entry(num).and_modify(|c| *c += 1).or_insert(1);
        }

        for (i, num) in nums.iter().enumerate() {
            lc.entry(num).and_modify(|c| *c += 1).or_insert(1);
            rc.entry(num).and_modify(|c| *c = c.saturating_sub(1));
            if lc[num] > (i + 1) / 2 && rc[num] > (nums.len() - i - 1) / 2 {
                return i as i32;
            }
        }

        -1
    }
}

fn main() {
    let tests = vec![
        (vec![1, 2, 2, 2], 2),
        (vec![2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4),
    ];

    for (nums, solution) in tests.into_iter() {
        let result = Solution::minimum_index(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
