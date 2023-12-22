// https://leetcode.com/problems/maximum-score-after-splitting-a-string

/** 
 * Don't really need HashMap, since each side only really needs to track the count
 * of a single digit. Could just use a single usize for left and right, and increment those.
 * 
 * Don't really feel like re-coding it, solution is otherwise the same. Would save some space.
 * */

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn max_score(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut l: HashMap<char, i32> = HashMap::with_capacity(chars.len());
        let mut r: HashMap<char, i32> = HashMap::with_capacity(chars.len());
        let mut mx = 0;

        for ch in chars.iter() {
            *r.entry(*ch).or_insert(0) += 1;
        }

        for ch in &chars[0..chars.len() - 1] {
            *r.get_mut(ch).unwrap() -= 1;
            *l.entry(*ch).or_insert(0) += 1;
            let score = l.get(&'0').unwrap_or(&0) + r.get(&'1').unwrap_or(&0);
            mx = i32::max(mx, score);
        }

        mx
    }
}

fn main() {
    let tests = vec![
        ("011101".to_string(), 5),
        ("00111".to_string(), 5),
        ("1111".to_string(), 3),
        ("00".to_string(), 1),
    ];

    for (s, solution) in tests {
        let result = Solution::max_score(s);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
