// https://leetcode.com/problems/partition-labels
struct Solution;

use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut m: HashMap<char, (usize, usize)> = HashMap::with_capacity(s.len());
        for (i, ch) in s.chars().enumerate() {
            m.entry(ch)
                .and_modify(|pair| {
                    let min = usize::min(i, pair.0);
                    let max = usize::max(i, pair.1);
                    *pair = (min, max);
                })
                .or_insert((i, i));
        }

        let mut intervals: VecDeque<(usize, usize)> = m.into_values().collect();
        intervals.make_contiguous().sort_by_key(|pair| pair.0);
        let mut out = Vec::with_capacity(intervals.len());

        while let Some(i) = intervals.pop_front() {
            let mut i = i;
            while let Some(j) = intervals.pop_front() {
                if i.1 <= j.0 {
                    intervals.push_front(j);
                    break;
                }
                i.1 = usize::max(i.1, j.1);
            }
            out.push((i.1 - i.0 + 1) as i32);
        }

        out
    }
}

fn main() {
    let tests = vec![("ababcbacadefegdehijhklij".to_string(), vec![9, 7, 8])];

    for (s, solution) in tests.into_iter() {
        let result = Solution::partition_labels(s);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
