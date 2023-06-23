// https://leetcode.com/problems/coin-change
struct Solution;

use std::collections::HashMap;

// Top-down DFS with caching of intermediary results. Basically same as
// 'climbing=starirs' problem.
impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut cache = HashMap::new();
        let min = Solution::step(&coins, amount, &mut cache);

        match min {
            Some(m) => m,
            None => -1,
        }
    }

    fn step(
        coins: &Vec<i32>,
        amount: i32, cache: &mut HashMap<i32, Option<i32>>
    ) -> Option<i32> {
        if amount < 0 {
            return None;
        } else if amount == 0 {
            return Some(0);
        }

        if let Some(val) = cache.get(&amount) {
            return *val;
        }

        let mut min: Option<i32> = None;
        for coin in coins.iter() {
            let opt = Solution::step(coins, amount - coin, cache);
            match (opt, min) {
                (None, _) => {},
                (Some(n), None) => min = Some(n + 1),
                (Some(n), Some(m)) =>  min = Some(i32::min(m, 1 + n)),
            }
        }
        cache.insert(amount, min);
        
        *cache.get(&amount).unwrap()
    }
}

fn main() {
    let tests = vec![
        (vec![1,2,5], 11, 3),
        (vec![2], 3, -1),
        (vec![1], 0, 0),
    ];

    for (coins, amount, solution) in tests {
        let result = Solution::coin_change(coins.clone(), amount);
        println!("coins={:?}, amount={:?}, solution={:?}, result={:?}",
            coins, amount, solution, result);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")


}
