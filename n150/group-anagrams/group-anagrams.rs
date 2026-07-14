// https://leetcode.com/problems/group-anagrams
struct Solution;

use std::collections::HashMap;

impl Solution {
    const ASCII_LOWERCASE: &str = "abcdefghijklmnopqrstuvwxyz";

    #[tracing::instrument(ret)]
    fn counts_to_key(map: HashMap<char, usize>) -> String {
        let mut key = String::with_capacity(map.len() * 3);
        for ch in Self::ASCII_LOWERCASE.chars() {
            if let Some(count) = map.get(&ch) {
                if !key.is_empty() {
                    key.push('-');
                }
                key.push(ch);
                key.push_str(&format!("{}", count));
            }
        }

        key
    }

    #[tracing::instrument(ret)]
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let pairs: Vec<(String, String)> = strs
            .into_iter()
            .map(|s| {
                let mut map = HashMap::new();
                for ch in s.chars() {
                    map.entry(ch).and_modify(|c| *c += 1).or_insert(1);
                }
                let key = Self::counts_to_key(map);

                (key, s)
            })
            .collect();

        let mut map: HashMap<String, Vec<String>> = HashMap::new();
        for (key, s) in pairs {
            match map.get_mut(&key) {
                Some(v) => {
                    v.push(s);
                }
                None => {
                    map.insert(key, vec![s]);
                }
            }
        }
        tracing::info!(map=?map, "grouped anograms");

        map.into_iter().map(|(_k, v)| v).collect()
    }
}

fn sorted(mut v: Vec<Vec<String>>) -> Vec<Vec<String>> {
    for i in v.iter_mut() {
        i.sort();
    }
    v.sort();

    v
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![(
        vec![
            "eat".to_string(),
            "tea".to_string(),
            "tan".to_string(),
            "ate".to_string(),
            "nat".to_string(),
            "bat".to_string(),
        ],
        vec![
            vec!["bat".to_string()],
            vec!["nat".to_string(), "tan".to_string()],
            vec!["ate".to_string(), "eat".to_string(), "tea".to_string()],
        ],
    )];

    for (strs, solution) in tests {
        let result = Solution::group_anagrams(strs);
        let result = sorted(result);
        let solution = sorted(solution);
        assert_eq!(result, solution);
    }
}
