// https://leetcode.com/problems/buy-two-chocolates

struct Solution;

impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        let mut min: (i32, i32) = (i32::MAX, i32::MAX);
        for price in prices {
            if price <= min.0 {
                min.1 = min.0;
                min.0 = price;
            } else if price < min.1 {
                min.1 = price;
            }
        }

        let diff = money - min.0 - min.1;
        if diff >= 0 {
            diff
        } else {
            money
        }
    }
}

fn main() {
    let tests = vec![(vec![1, 2, 2], 3, 0), (vec![3, 2, 3], 3, 3)];

    for (prices, money, solution) in tests {
        let result = Solution::buy_choco(prices, money);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
