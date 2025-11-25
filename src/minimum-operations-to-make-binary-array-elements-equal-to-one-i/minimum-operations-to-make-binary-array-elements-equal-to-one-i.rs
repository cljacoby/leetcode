// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut q: VecDeque<usize> = VecDeque::with_capacity(nums.len());
        let mut count = 0;
        let len = nums.len();

        for (i, num) in nums.into_iter().enumerate() {
            while q.len() > 0 && i > q.front().unwrap() + 2 {
                q.pop_front();
            }

            if (num + q.len() as i32) % 2 == 0 {
                if i + 2 >= len {
                    return -1
                }
                count += 1;
                q.push_back(i);
            }
        }

        count
    }
}

fn main() {
    let tests = vec![
        (vec![0,1,1,1,0,0], 3),
        (vec![0,1,1,1], -1),
    ];

    for (nums, solution) in tests {
        let result = Solution::min_operations(nums);
        assert_eq!(result, solution);
    };

    println!("✅ All tests passed")
}
