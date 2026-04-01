#![allow(dead_code)]

// https://leetcode.com/problems/coin-change-ii
struct Solution;

use tracing_tree::HierarchicalLayer;
use tracing_subscriber::EnvFilter;
use tracing_subscriber::{Registry, prelude::*};

/** 
 * Invalid solution due to runtime complexity.
 * However, the handling of `pre` and `i` arguments to slice the array and only
 * select coins after a current prefix highlights the understanind of how to get
 * all combinations, as opposed to all permutations.
 * */
struct S;
impl S {
    #[tracing::instrument(ret)]
    fn step(pre: usize, curr: i32, target: i32, coins: &Vec<i32>) -> usize {
        if curr == target {
            return 1;
        } else if curr > target {
            return 0;
        }

        let mut sum = 0;
        for (i, val) in coins[pre..].iter().enumerate() {
            let count = Self::step(pre + i, curr + val, target, coins);
            sum += count;
        }

        sum
    }

    #[tracing::instrument(ret)]
    pub fn change(target: i32, coins: Vec<i32>) -> i32 {
        i32::try_from(Self::step(0, 0, target, &coins))
            .expect("failed conversion of usize to i32")
    }
}


/** 
 * 1D knapstack style solution.
 *
 * We create a 1D dynamic programming memo, and use a bottom up method.
 * Each index in the memo represents the total number of coing combinations
 * which could total to the amount equal to the DP index. The recurrance
 * looks like:
 *
 * dp[amt] = sum (dp[amt - Ci] ) for each Ci where Ci <=amt and i >= j
 * dp[0] = 1
 *
 * The key is structuing the two loops with the coins iteration on the outside,
 * which has the effect of the `pre` and `i` arguments in the polynomial solution,
 * which is we only use coins equal to or ahead of the current coin iteration, not
 * past coins as well.
 *
 * */
impl Solution {
    #[tracing::instrument(ret)]
    pub fn change(target: i32, coins: Vec<i32>) -> i32 {
        let coins: Vec<usize> = coins.into_iter()
            .map(|c| c.try_into().expect("coins i32 to usize failed"))
            .collect();

        let mut dp = vec![0; target as usize + 1];
        dp[0] = 1;
        
        // outer loop: iterate over each coin
        for c in coins.iter() {
            // inner loop: iterate over each amount. inner loop iteration variable is our dp memo index.
            for amt in 1..(dp.len()) {
                if amt >= *c {
                    dp[amt] += dp[amt - c]
                }
                tracing::info!(c=?c, amt=?amt, dp=?dp, "dp");
            }
        }

        *dp.last().expect("failed to pull final dp index")
    }
}

// todo: do the 2d knapsack solution as well, to solidify understanding

fn main() {
    Registry::default()
        .with(EnvFilter::from_default_env())
        .with(HierarchicalLayer::new(2).with_targets(true))
        .init();

    let tests = vec![
        (
            5,
            vec![1,2,5],
            4,
        ),
        (
            3,
            vec![2],
            0,
        ),
        (
            10,
            vec![10],
            1,
        ),
        (
            500,
            vec![3,5,7,8,9,10,11],
            35502874,
        ),
    ];

    for (target, coins, solution) in tests {
        let result = Solution::change(target, coins);
        assert_eq!(result, solution)
    }
}
