// https://leetcode.com/problems/valid-anagram

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn char_counts(s: String) -> HashMap<char, usize> {
        let mut map = HashMap::with_capacity(s.len());
        for ch in s.chars() {
            *map.entry(ch).or_insert(0) += 1;
        }

        map
    }

    pub fn is_anagram(s: String, t: String) -> bool {
        let s_map = Self::char_counts(s);
        let t_map = Self::char_counts(t);

        s_map == t_map
    }
}

fn main() {
    let tests = vec![
        ("anagram".to_string(), "nagaram".to_string(), true),
        ("car".to_string(), "rat".to_string(), false),
    ];

    for (s, t, solution) in tests {
        let result = Solution::is_anagram(s, t);
        assert_eq!(result, solution);
    }
}
