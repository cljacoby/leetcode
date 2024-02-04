// https://leetcode.com/problems/minimum-window-substring
struct Solution;

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn charfreq(word: &String) -> HashMap<char, usize> {
        let mut freq = HashMap::new();
        for ch in word.chars() {
            *freq.entry(ch).or_insert(0) += 1;
        }

        freq
    }

    pub fn valid_win(freq_win: &HashMap<char, usize>, freq_t: &HashMap<char, usize>) -> bool {
        for (ch, t_count) in freq_t.iter() {
            match freq_win.get(&ch) {
                None => return false,
                Some(win_count) => {
                    if win_count < t_count {
                        return false;
                    }
                }
            }
        }

        true
    }

    pub fn min_window(s: String, t: String) -> String {
        let freq_t = Self::charfreq(&t);
        let mut freq_win: HashMap<char, usize> = HashMap::new();
        let mut win: VecDeque<char> = VecDeque::new();
        let mut min_win: Option<String> = None;

        for ch in s.chars() {
            // println!("ch={:?}, freq_t={:?}, win={:?}, freq_win={:?}", ch, freq_t, win, freq_win);
            if !freq_t.contains_key(&ch) && win.is_empty() {
                continue;
            }
            win.push_back(ch);
            if freq_t.contains_key(&ch) {
                *freq_win.entry(ch).or_insert(0) += 1;
                while freq_win.get(&ch).unwrap_or(&0) >= freq_t.get(&ch).unwrap_or(&0) {
                    if freq_t.contains_key(&win[0]) && freq_win[&win[0]] <= freq_t[&win[0]] {
                        break;
                    }
                    let out = win.pop_front().unwrap();
                    if let Some(count) = freq_win.get_mut(&out) {
                        *count -= 1;
                        if *count == 0 {
                            freq_win.remove(&out);
                        }
                    }
                }
            }

            if Self::valid_win(&freq_win, &freq_t) {
                match min_win {
                    None => min_win = Some(win.iter().collect()),
                    Some(ref s) => {
                        if win.len() < s.len() {
                            min_win = Some(win.iter().collect())
                        }
                    }
                }
            }
        }

        min_win.unwrap_or("".to_string())
    }
}

fn main() {
    let tests = vec![
        (
            "ADOBECODEBANC".to_string(),
            "ABC".to_string(),
            "BANC".to_string(),
        ),
        ("a".to_string(), "a".to_string(), "a".to_string()),
        ("a".to_string(), "aa".to_string(), "".to_string()),
    ];

    for (s, t, solution) in tests {
        let result = Solution::min_window(s, t);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
