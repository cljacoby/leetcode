// https://leetcode.com/problems/destination-city
struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let mut s_src = HashSet::with_capacity(paths.len());
        let mut s_dest = HashSet::with_capacity(paths.len());

        for mut pair in paths {
            let dest = pair.pop().unwrap();
            let src = pair.pop().unwrap();
            s_src.insert(src);
            s_dest.insert(dest);
        }

        let d: Vec<_> = s_dest.difference(&s_src).collect();
        assert_eq!(d.len(), 1, "Did not find 1 destination");

        d[0].to_owned()
    }
}

fn main() {
    let tests = vec![(
        vec![
            vec!["London".to_string(), "New York".to_string()],
            vec!["New York".to_string(), "Lima".to_string()],
            vec!["Lima".to_string(), "Sao Paulo".to_string()],
        ],
        "Sao Paulo".to_string(),
    )];


    for (paths, solution) in tests {
        let result = Solution::dest_city(paths);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
