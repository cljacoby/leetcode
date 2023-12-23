// https://leetcode.com/problems/path-crossing

struct Solution;

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let dirs = HashMap::from([
            ('N', (1, 0)),
            ('E', (0, 1)),
            ('S', (-1, 0)),
            ('W', (0, -1))
        ]);

        let path: Vec<char> = path.chars().collect();
        let mut visited = HashSet::with_capacity(path.len());
        let mut pos = (0, 0);
        visited.insert(pos.clone());

        for ch in path {
            let (v, h) = dirs.get(&ch).unwrap();
            pos.0 += v;
            pos.1 += h;
            if visited.contains(&pos) {
                return true;
            }
            visited.insert(pos.clone());
        }

        false
    }
}

fn main() {
    let tests = vec![("NES".to_string(), false), ("NESWW".to_string(), true)];
    for (s, solution) in tests {
        let result = Solution::is_path_crossing(s);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
