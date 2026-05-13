// https://leetcode.com/problems/contains-duplicate
struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::with_capacity(nums.len());
        for num in nums.into_iter() {
            if set.contains(&num) {
                return true;
            }
            set.insert(num);
        }

        false
    }
}

fn main() {
    let tests = vec![
        (
            vec![1,2,3,1],
            true,
        ),
        (
            vec![1,2,3,4],
            false
        ),
        (
            vec![1,1,1,3,3,4,3,2,4,2],
            true,
        )
    ];

    for (nums, solution) in tests {
        let result = Solution::contains_duplicate(nums);
        assert_eq!(result, solution);
    }

}
