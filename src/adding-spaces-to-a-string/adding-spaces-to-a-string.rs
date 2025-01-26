// https://leetcode.com/problems/adding-spaces-to-a-string

struct Solution;
struct Solution2;

use std::collections::{HashSet, VecDeque};

// First Solution. Using intuition + regular data strucures.
impl Solution {
    pub fn add_spaces(s: String, spaces: Vec<i32>) -> String {
        let mut s: VecDeque<char> = s.chars().collect();
        let mut out = Vec::with_capacity(s.len() + spaces.len());
        let spaces: HashSet<i32> = spaces.into_iter().collect();
        let mut i = 0;

        while let Some(ch) = s.pop_front() {
            if spaces.contains(&i) {
                out.push(' ');
            }
            out.push(ch);
            i += 1;
        }

        out.into_iter().collect()
    }
}

// Second Solution. Leetcode "optimized".
impl Solution2 {
    pub fn add_spaces(s: String, spaces: Vec<i32>) -> String {
        let mut out = Vec::with_capacity(s.len() + spaces.len());
        let mut i_space = 0;

        for (i, ch) in s.chars().enumerate() {
            if i_space < spaces.len() && 
                i as i32 == spaces[i_space]
            {
                out.push(' ');
                i_space += 1;
            }
            out.push(ch);
        }

        out.into_iter().collect()
    }
}

fn main() {
    let tests = vec![
        (
            "LeetcodeHelpsMeLearn".to_string(),
            vec![8, 13, 15],
            "Leetcode Helps Me Learn".to_string(),
        ),
        (
            "icodeinpython".to_string(),
            vec![1, 5, 7, 9],
            "i code in py thon".to_string(),
        ),
    ];

    for (s, spaces, solution) in tests {
        let result = Solution::add_spaces(s.clone(), spaces.clone());
        assert_eq!(result, solution);
        let result = Solution2::add_spaces(s, spaces);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
