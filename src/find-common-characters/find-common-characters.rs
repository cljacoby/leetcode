// https://leetcode.com/problems/find-common-characters
struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

/**
 * According to leetcode history, I apparently wrote this
 * on Oct 29, 2020. No recollection of it. Intersting use of
 * break-to-labelled-loop feature by former self.
 * */

impl Solution {
    pub fn char_counts(s: &String) -> HashMap<char, u32> {
        let mut map = HashMap::new();
        for c in s.chars() {
            map.entry(c).and_modify(|i| *i += 1).or_insert(1);
        }

        map
    }

    pub fn common_chars(words: Vec<String>) -> Vec<String> {
        let counts: Vec<HashMap<char, u32>> = words.iter()
            .map(|s| Solution::char_counts(s))
            .collect();
        let char_set: HashSet<char> = words.iter()
            .map(|s| s.chars())
            .flatten()
            .collect();
        let mut out: Vec<String> = vec![];
        let mut iterchars = char_set.iter();
        'outer: loop {
            if let Some(c) = iterchars.next() {
                let mut lowest = std::u32::MAX;
                for map in counts.iter() {
                    lowest = match map.get(&c) {
                        None => continue 'outer,
                        Some(count) => {
                            if lowest < *count {
                                lowest
                            } else {
                                *count
                            }
                        }
                    };
                }
                for _ in 0..lowest {
                    out.push(c.to_string());
                }
            } else {
                // Iterator exhausted
                break 'outer;
            }
        }

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![
                "bella".to_string(),
                "label".to_string(),
                "roller".to_string(),
            ],
            vec!["e".to_string(), "l".to_string(), "l".to_string()],
        ),
        (
            vec![
                "cool".to_string(),
                "lock".to_string(),
                "cook".to_string()
            ],
            vec!["c".to_string(), "o".to_string()],
        ),
    ];

    for (words, mut solution) in tests {
        let mut result = Solution::common_chars(words);
        result.sort();
        solution.sort();
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
