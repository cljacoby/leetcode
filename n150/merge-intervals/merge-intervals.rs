// https://leetcode.com/problems/merge-intervals
struct Solution;

use std::collections::VecDeque;

struct Interval(i32, i32);

impl From<Vec<i32>> for Interval {
    fn from(arr: Vec<i32>) -> Self {
        assert_eq!(arr.len(), 2);
        let a = arr[0];
        let b = arr[1];

        Self(a, b)
    }
}

impl From<Interval> for Vec<i32> {
    fn from(interval: Interval) -> Vec<i32> {
        vec![interval.0, interval.1]
    }
}

impl Solution {
    #[tracing::instrument(ret)]
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by_key(|arr| arr[0]);

        let mut intervals: VecDeque<Interval> = intervals.into_iter()
            .map(|arr| Interval::from(arr))
            .collect();
        
        let mut out = vec![]; 

        while let Some(interval) = intervals.pop_front() {
            match out.last_mut() {
                None => out.push(interval),
                Some(last) => {
                    if last.1 >= interval.0 {
                        last.1 = i32::max(last.1, interval.1)
                    } else {
                        out.push(interval);
                    }
                }
            }
        }

        out.into_iter()
            .map(|interval| interval.into())
            .collect()
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![vec![1,3],vec![2,6],vec![8,10],vec![15,18]],
            vec![vec![1,6],vec![8,10],vec![15,18]],
        ),
        (
            vec![vec![1,4],vec![4,5]],
            vec![vec![1,5]],
        ),
    ];

    for (intervals, solution) in tests {
        let result = Solution::merge(intervals);
        assert_eq!(result, solution);
    }
}
