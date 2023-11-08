// https://leetcode.com/problems/find-the-winner-of-an-array-game

use std::collections::VecDeque;

struct Solution;

impl Solution {
    pub fn get_winner(arr: Vec<i32>, k: i32) -> i32 {
        let mut x = arr[0];
        let mut q = VecDeque::with_capacity(arr.len());
        q.extend(&arr[1..]);

        let mut wins = 0;
        while wins < k {
            if x > q[0] {
                let loser = q.pop_front().unwrap();
                q.push_back(loser);
                wins += 1;
            }
            else if x == q[0] {
                unreachable!("Values should have been all unique");
            } else {
                q.push_back(x);
                x = q.pop_front().unwrap();
                wins = 1;
            }
        }

        return x;
    }
}

fn main() {
    let tests = vec![
        (vec![2,1,3,5,4,6,7], 2, 5),
        (vec![3,1,2], 10, 3),
    ];
    for (arr, k, solution) in tests {
        let result = Solution::get_winner(arr, k);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed");
}
