// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let thresh = arr.len() as f64 * 0.25;
        let mut freq = HashMap::with_capacity(arr.len());

        for num in arr.iter() {
            let count = freq.entry(num).or_insert(0);
            *count += 1;
            if *count as f64 > thresh {
                return *num;
            }
        }

        unreachable!("No element with 25% frequency, arr={:?}", arr);
    }
}

fn main() {
    let tests = vec![
        (vec![1, 2, 2, 6, 6, 6, 6, 7, 10], 6),
        (vec![1, 1], 1),
        (vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12], 12),
        (vec![1], 1),
    ];

    for (arr, solution) in tests {
        let result = Solution::find_special_integer(arr);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
