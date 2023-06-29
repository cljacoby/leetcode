// https://leetcode.com/problems/best-time-to-buy-and-sell-stock
struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min = i32::MAX;
        let mut max = i32::MIN;
        let mut diff = 0;

        for p in prices.iter() {
            let p = *p;
            if p < min {
                min = p;
                max = p;
            }
            min = i32::min(p, min);
            max = i32::max(p, max);
            diff = i32::max(diff, max - min);
        }

        diff
    }
}

fn main() {
    let tests = vec![
        (vec![7,1,5,3,6,4], 5),
        (vec![7,6,4,3,1], 0),
    ];


    for (prices, solution) in tests {
        let result = Solution::max_profit(prices);
        assert_eq!(result, solution);
    }

}
