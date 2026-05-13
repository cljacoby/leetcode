// https://leetcode.com/problems/insert-interval
struct Solution;

use std::collections::VecDeque;

struct Interval {
    start: i32,
    end: i32,
}

impl From<Vec<i32>> for Interval {
    fn from(arr: Vec<i32>) -> Self {
        assert_eq!(arr.len(), 2, "interval input was not vec of length 2");
        let start = arr[0];
        let end = arr[1];

        Self { start, end }
    }
}

impl From<Interval> for Vec<i32> {
    fn from(interval: Interval) -> Vec<i32> {
        vec![interval.start, interval.end]
    }
}

impl Solution {

    #[tracing::instrument(ret)]
    pub fn insert(
        intervals: Vec<Vec<i32>>,
        insert: Vec<i32>
    ) -> Vec<Vec<i32>> {
        let intervals: Vec<Interval> = intervals.into_iter()
            .map(|x| Interval::from(x))
            .collect();
        let mut insert = Interval::from(insert);
        let partition = intervals.partition_point(|interval| interval.end < insert.start);
        let mut left = intervals;
        let mut right = VecDeque::from(left.split_off(partition));

        while let Some(interval) = right.pop_front() {
            if interval.start <= insert.end {
                insert.start = i32::min(interval.start, insert.start);
                insert.end = i32::max(interval.end, insert.end)
            } else {
                right.push_front(interval);
                break;
            }
        }

        left.push(insert);
        left.extend(right);

        left.into_iter()
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
            vec![vec![1,3],vec![6,9]],
            vec![2,5],
            vec![vec![1,5],vec![6,9]]
        ),
        (
            vec![vec![2,3],vec![6,9]],
            vec![1,5],
            vec![vec![1,5],vec![6,9]]
        ),
        (
            vec![vec![1,2],vec![3,5],vec![6,7],vec![8,10],vec![12,16]],
            vec![4,8],
            vec![vec![1,2],vec![3,10],vec![12,16]],
        ),
        (
            vec![vec![1,2],vec![12,16]],
            vec![4,8],
            vec![vec![1,2],vec![4,8],vec![12,16]],
        ),
    ];

    for (intervals, insert, solution) in tests {
        let result = Solution::insert(intervals, insert);
        assert_eq!(result, solution);
    }

}
