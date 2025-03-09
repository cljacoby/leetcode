// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks
struct Solution;

use std::collections::{VecDeque, HashMap};

impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let size = k as usize;
        let mut window = VecDeque::with_capacity(size);
        let mut counts: HashMap<char, usize> = HashMap::from_iter([
            ('W', 0),
            ('B', 0),
        ]);
        let mut min = usize::MAX;

        for ch in blocks.chars() {
            if window.len() == size {
                let ch_out = window.pop_front().unwrap();
                counts.entry(ch_out).and_modify(|c| *c -= 1);
            }

            window.push_back(ch);
            counts.entry(ch).and_modify(|c| *c += 1);

            if window.len() == size {
                min = usize::min(min, counts[&'W']);
            }
        }

        min as i32
    }
}

fn main() {
    let tests = vec![
        ("WBBWWBBWBW".to_string(), 7, 3),
        ("WBWBBBW".to_string(), 2, 0),
    ];

    for (s, k, solution) in tests.into_iter() {
        let result = Solution::minimum_recolors(s, k);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
