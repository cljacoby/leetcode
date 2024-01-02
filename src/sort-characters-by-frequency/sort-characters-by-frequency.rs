// https://leetcode.com/problems/sort-characters-by-frequency

#![allow(dead_code)]

use std::collections::{HashMap, BinaryHeap};

// Frequency HashMap + Sort on the values
struct Solution1;
impl Solution1 {
    pub fn frequency_sort(s: String) -> String {
        let mut counts = HashMap::new();
        for ch in s.chars() {
            *counts.entry(ch).or_insert(0) += 1;
        }
        let mut sorted: Vec<(char, usize)> = counts.into_iter().collect();
        sorted.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
 
        sorted.into_iter()
            .map(|(ch, count)| vec![ch; count])
            .flatten()
            .collect()
    }
}

// Frequency HashMap + BinaryHeap for the ordering
struct Solution;
impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let mut counts = HashMap::new();
        for ch in s.chars() {
            *counts.entry(ch).or_insert(0) += 1;
        }
        let mut pq: BinaryHeap<(usize, char)> = BinaryHeap::new();
        for (ch, count) in counts {
            pq.push((count, ch));
        }
        let mut chars: Vec<char> = vec![];
        while let Some((count, ch)) = pq.pop() {
            for _ in 0..count {
                chars.push(ch);
            }
        }

        chars.into_iter().collect()
    }
}

fn main() {
    let tests = [
        ("cccaaa".to_string(), "cccaaa".to_string()),
        ("Aabb".to_string(), "bbaA".to_string()),
    ];

    for (s, solution) in tests {
        let result = Solution::frequency_sort(s);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
