// https://leetcode.com/problems/longest-consecutive-sequence
struct Solution;

use std::collections::HashSet;

impl Solution {

    #[tracing::instrument(ret)]
    fn seq(num: i32, set: &mut HashSet<i32>) -> i32 {
        let mut count = 1;
        let mut i = num;
        set.remove(&num);

        while set.contains(&(i + 1)) {
            count += 1;
            i += 1;
            set.remove(&i);
        }

        let mut i = num;
        while set.contains(&(i - 1)) {
            count += 1;
            i -= 1;
            set.remove(&i);
        }

        count
    }

    #[tracing::instrument(ret)]
    fn first(set: &HashSet<i32>) -> Option<i32> {
        set.iter().next().map(|n| n.to_owned())
    }

    #[tracing::instrument(ret)]
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut set = HashSet::new(); 
        let mut max = 0;

        for num in nums.iter() {
            set.insert(*num);
        }

        while let Some(num) = Self::first(&set) {
            let seq = Self::seq(num, &mut set);
            max = i32::max(seq, max);
        }

        max
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![100,4,200,1,3,2],
            4,
        ),
        (
            vec![0,3,7,2,5,8,4,6,0,1],
            9,
        ),
        (
            vec![1,0,1,2],
            3,
        ),
    ];

    for (nums, solution) in tests {
        let result = Solution::longest_consecutive(nums);
        assert_eq!(result, solution);
    }
}
