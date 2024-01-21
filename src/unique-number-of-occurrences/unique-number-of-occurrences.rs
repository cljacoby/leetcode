// https://leetcode.com/problems/unique-number-of-occurrences
struct Solution;

use std::collections::{HashMap, HashSet};

impl Solution {

    pub fn freq(arr: &Vec<i32>) -> HashMap<i32, usize> {
        let mut freq = HashMap::new();
        for i in arr.iter() {
            *freq.entry(*i).or_insert(0) += 1;
        }

        freq
    }

    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let freq = Self::freq(&arr);
        let mut seen = HashSet::new();
        for (_, v) in freq.iter() {
            if seen.contains(v) {
                return false;
            }
            seen.insert(*v);
        }
        
        true
    }
}

fn main() {
    let tests = vec![
        (vec![1,2,2,1,1,3], true),
        (vec![1,2,], false),
    ];

    for (arr, solution) in tests {
        let result = Solution::unique_occurrences(arr);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
