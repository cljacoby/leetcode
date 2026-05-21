// https://leetcode.com/problems/valid-anagram
struct Solution;

use std::collections::HashMap;

impl Solution {
    fn string_to_counts(s: String) -> HashMap<char, usize> {
        let mut counts = HashMap::new();
        for ch in s.chars() {
            counts.entry(ch)
                .and_modify(|c| *c += 1)
                .or_insert(1);
        }

        counts
    }

    pub fn is_anagram(s: String, t: String) -> bool {
        let a = Self::string_to_counts(s);
        let b = Self::string_to_counts(t);

        a == b
    }
}

fn main() {
    let tests = vec![
        ("anagram".to_string(), "nagaram".to_string(), true),
    ];

    for (s, t, solution) in tests {
        let result = Solution::is_anagram(s, t);
        assert_eq!(result, solution);
    }
}
