// https://leetcode.com/problems/largest-substring-between-two-equal-characters
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn max_length_between_equal_characters(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut map: HashMap<char, (i32, i32)> = HashMap::with_capacity(chars.len());
        let mut sol: i32 = -1;

        for (i, ch) in chars.iter().enumerate() {
            let i = i as i32;
            if let Some((mn, mx)) = map.get_mut(&ch) {
                *mn = i32::min(*mn, i);
                *mx = i32::max(*mx, i);
                sol = i32::max(sol, *mx - *mn - 1);
            } else {
                map.insert(*ch, (i, i));
            }
        }

        sol
    }
}

fn main() {
    let tests = vec![
        ("aa".to_string(), 0),
        ("abca".to_string(), 2),
        ("cbzxy".to_string(), -1),
    ];

    for (s, solution) in tests {
        let result = Solution::max_length_between_equal_characters(s);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
