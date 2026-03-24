// https://leetcode.com/problems/longest-substring-without-repeating-characters
struct Solution;

use std::collections::{VecDeque, HashSet};

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut set = HashSet::with_capacity(s.len());
        let mut window = VecDeque::with_capacity(s.len());
        let mut max = 0;

        for ch in s.chars() {
            while set.contains(&ch) {
                let out = window.pop_front().expect("window and set size mismatch");
                set.remove(&out);
            }
            set.insert(ch);
            window.push_back(ch);
            max = i32::max(max, window.len() as i32);
        }

        max
    }
}

fn main() {
    let tests = vec![
        (
            "abcabcbb".to_string(),
            3,
        ),
        (
            "bbbbbbbb".to_string(),
            1,
        ),
        (
            "pwwkew".to_string(),
            3,
        ),
    ];

    for (s, solution) in tests {
        let result = Solution::length_of_longest_substring(s);
        assert_eq!(result, solution);
    }
}
