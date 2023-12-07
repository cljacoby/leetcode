// https://leetcode.com/problems/calculate-money-in-leetcode-bank
struct Solution;

impl Solution {
    pub fn total_money(n: i32) -> i32 {
        let mut total = 0;
        let mut add = 0;
        for i in 0..n {
            if i % 7 == 0 {
                add += 1;
            }
            total += add + i % 7;
        }
        
        total
    }
}

fn main() {
    let tests = vec![
        (4, 10),
        (10, 37),
        (20, 96),
    ];
    for (days, solution) in tests {
        let result = Solution::total_money(days);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
