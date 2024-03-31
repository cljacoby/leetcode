// https://leetcode.com/problems/intersection-of-two-arrays
struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let s1: HashSet<i32> = HashSet::from_iter(nums1.into_iter());
        let s2: HashSet<i32> = HashSet::from_iter(nums2.into_iter());

        s1.intersection(&s2).map(|i| i.to_owned()).collect()
    }
}

fn main() {
    let tests = vec![
        (vec![1, 2, 2, 1], vec![2, 2], vec![2]),
        (vec![4,9,5], vec![9,4,9,8,4], vec![9,4])
    ];

    for (nums1, nums2, solution) in tests {
        let result = Solution::intersection(nums1, nums2);
        assert_eq!(result, solution);
    }
}
