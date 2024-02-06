// https://leetcode.com/problems/first-unique-character-in-a-string

struct Solution;
struct Solution1;

use std::collections::HashMap;

// First solution. Conventional approach using HashMap.
impl Solution1 {
    pub fn freqmap(s: &String) -> HashMap<char, usize> {
        let mut freq = HashMap::new();
        for ch in s.chars() {
            *freq.entry(ch).or_insert(0) += 1;
        }

        freq
    }

    pub fn first_uniq_char(s: String) -> i32 {
        let freq = Self::freqmap(&s);
        for (i, ch) in s.chars().enumerate() {
            if let Some(count) = freq.get(&ch) {
                if *count == 1 {
                    return i as i32;
                }
            }
        }

        -1
    }
}

// Second solution. Leetcoderific solution. Objectively worse code. Runs slightly faster.
impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut counts: [usize; 32] = [0; 32];
        for ch in s.chars() {
            counts[ch as usize - 97] += 1;
        }
        for (i, ch) in s.chars().enumerate() { 
            if counts[ch as usize - 97] == 1 {
                return i as i32;
            }
        }

        -1
    }
}

fn main() {
    // Solution::method(...);
    let tests = vec![
        ("leetcode".to_string(), 0),
        ("loveleetcode".to_string(), 2),
        ("aabb".to_string(), -1),
    ];

    for (s, solution) in tests {
        let result = Solution::first_uniq_char(s.clone());
        assert_eq!(result, solution);
        let result = Solution1::first_uniq_char(s);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
