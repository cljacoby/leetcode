// https://leetcode.com/problems/find-words-containing-character
struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let words: Vec<HashSet<char>> = words.into_iter()
            .map(|w| HashSet::from_iter(w.chars()))
            .collect();
        let mut idx = vec![];
        for (i, w) in words.iter().enumerate() {
            if w.contains(&x) {
                idx.push(i as i32);
            }
        }

        idx
    }
}

fn main() {
    let tests = vec![
        (vec!["leet".to_string(),"code".to_string()], 'e', vec![0,1]),
    ];

    for (words, x, solution) in tests {
        let result = Solution::find_words_containing(words, x);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
