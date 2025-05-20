// https://leetcode.com/problems/type-of-triangle
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn valid_sides(a: i32, b: i32, c: i32) -> bool {
        (a + b > c)
            && (a + c > b)
            && (b + c > a)
    }

    pub fn triangle_type(nums: Vec<i32>) -> String {
        let (a, b, c) = (nums[0], nums[1], nums[2]);
        if !Self::valid_sides(a, b, c) {
            return "none".to_string();
        }

        let mut counts = HashMap::with_capacity(3);
        for num in nums.into_iter() {
            counts.entry(num).and_modify(|c| *c += 1).or_insert(1);
        }

        match counts.len() {
            1 => "equilateral".to_string(),
            2 => "isosceles".to_string(),
            3 => "scalene".to_string(),
            _ => panic!("bad input data")
        }
    }
}

fn main() {
    let tests = vec![
        (vec![3, 3, 3], "equilateral".to_string()),
        (vec![2, 3, 4], "scalene".to_string()),
        (vec![2, 2, 3], "isosceles".to_string()),
    ];

    for (nums, solution) in tests {
        let result = Solution::triangle_type(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
