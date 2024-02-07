// https://leetcode.com/problems/group-anagrams
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<Vec<char>, Vec<String>> = HashMap::new();

        for s in strs {
            let mut v: Vec<char> = s.chars().collect();
            v.sort();
            map.entry(v).or_insert(vec![]).push(s);
        }

        map.into_iter().map(|(_k, v)| v).collect()
    }
}

fn main() {
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

    // Writing a test assertion is a pain in the butt for this one, so we're just manually
    // inspecting the output and submitting it.

    for (strings, solution) in tests {
        let result = Solution::group_anagrams(strings.clone());
        println!("solution = {:?}", solution);
        println!("result = {:?}", result);
    }
}
