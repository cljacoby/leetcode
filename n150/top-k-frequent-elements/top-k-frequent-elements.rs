// https://leetcode.com/problems/top-k-frequent-elements
struct Solution;

use std::collections::HashMap;

impl Solution {

    #[tracing::instrument(ret)]
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let b = nums.len() + 1;

        let mut counts: HashMap<i32, usize> = HashMap::new();
        for num in nums {
            counts.entry(num)
                .and_modify(|c| *c += 1)
                .or_insert(1);
        }
        tracing::info!(counts=?counts);

        let mut buckets: Vec<Vec<i32>> = vec![vec![]; b];
        for (num, count) in counts.iter() {
            buckets[*count].push(*num);
        }
        tracing::info!(buckets=?buckets);

        // I get so happy when I find a reason to use break-to-outer-labelled loop
        let mut out = Vec::with_capacity(k);
        'outer: while let Some(mut bucket) = buckets.pop() {
            while let Some(num) = bucket.pop() {
                out.push(num);
                if out.len() == k {
                    break 'outer
                }
            }
        }
        assert_eq!(out.len(), k, "did not find at least `k` elements to return");
    
        out
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![1,2,1,2,1,2,3,1,3,2],
            2,
            vec![2,1],
        ),
        (
            vec![1,1,1,2,2,3],
            2,
            vec![1,2],
        ),
        (
            vec![1],
            1,
            vec![1],
        ),
    ];

    for (nums, k, solution) in tests {
        let result = Solution::top_k_frequent(nums, k);
        // ordering makes assert_eq!() slightly annoying. this solution
        // passes when submitted.
        tracing::info!(result=?result, solution=?solution);
    }
}
