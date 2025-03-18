struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        if nums.len() % 2 != 0 {
            return false;
        }

        let mut map = HashMap::with_capacity(nums.len() / 2);
        for num in nums.into_iter() {
            map.entry(num)
                .and_modify(|c| *c += 1)
                .or_insert(1);
        }

        for val in map.values() {
            if val % 2 != 0 {
                return false;
            }
        }

        true
    }
}

fn main() {
    let tests = vec![
        (vec![3,2,3,2,2,2], true),
        (vec![1,2,3,4], false),
    ];

    for (nums, solution) in tests.into_iter() {
        let result = Solution::divide_array(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
