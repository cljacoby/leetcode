// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn good_word(word: &String, mut counts: HashMap<char, usize>) -> bool {
        for ch in word.chars() {
            match counts.get_mut(&ch) {
                None => {
                    return false;
                }
                Some(count) => {
                    *count -= 1;
                    if *count == 0 {
                        counts.remove(&ch);
                    }
                }
            }
        }

        true
    }

    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let mut counts: HashMap<char, usize> = HashMap::with_capacity(chars.len());
        for ch in chars.chars() {
            let count = counts.entry(ch).or_insert(0);
            *count += 1;
        }

        let mut length = 0;
        for word in words {
            if Solution::good_word(&word, counts.clone()) {
                length += word.len();
            }
        }

        length as i32
    }
}

fn main() {
    // Solution::method(...);
    let tests = vec![
        (
            vec![
                "cat".to_string(),
                "bt".to_string(),
                "hat".to_string(),
                "tree".to_string(),
            ],
            "atach".to_string(),
            6,
        ),
        (
            vec![
                "hello".to_string(),
                "world".to_string(),
                "leetcode".to_string(),
            ],
            "welldonehoneyr".to_string(),
            10,
        ),
    ];


    for (words, chars, solution) in tests {
        let result = Solution::count_characters(words, chars);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
