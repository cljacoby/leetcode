// https://leetcode.com/problems/partition-array-according-to-given-pivot
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn pivot_array(nums: Vec<i32>, p: i32) -> Vec<i32> {
        let mut left = vec![];
        let mut pivot = vec![];
        let mut right = vec![];
        let mut nums = VecDeque::from(nums);


        while let Some(num) = nums.pop_front() {
            if num < p {
                left.push(num);
            } else if num == p {
                pivot.push(num);
            } else {
                right.push(num);
            }
        }

        left.extend(pivot);
        left.extend(right);

        left
    }
}

struct Solution2;
impl Solution2 {
    pub fn pivot_array(nums: Vec<i32>, p: i32) -> Vec<i32> {
        let mut left = vec![];
        let mut pivot = vec![];
        let mut right = vec![];


        for num in nums.into_iter() {
            if num < p {
                left.push(num);
            } else if num == p {
                pivot.push(num);
            } else {
                right.push(num);
            }
        }

        left.extend(pivot);
        left.extend(right);

        left
    }
}

struct Solution3;
impl Solution3 {
    pub fn pivot_array(nums: Vec<i32>, p: i32) -> Vec<i32> {
        let len = nums.len();
        let mut out = vec![0; nums.len()];
        let mut l = 0;
        let mut r = len - 1;

        for (i, j) in (0..len).zip((0..len).rev()) {
            if nums[i] < p {
                out[l] = nums[i];
                l += 1;
            }
            if nums[j] > p {
                out[r] = nums[j];
                r -= 1;
            }
        }

        out[l..=r].fill(p);

        out
    }
}

fn main() {
    let tests = vec![
        (vec![9,12,5,10,14,3,10], 10, vec![9,5,3,10,10,12,14]),
        (vec![-3,4,3,2], 2, vec![-3,2,4,3]),
    ];

    for (nums, pivot, solution) in tests.clone() {
        let result = Solution::pivot_array(nums, pivot);
        assert_eq!(result, solution);
    }
    for (nums, pivot, solution) in tests.clone() {
        let result = Solution2::pivot_array(nums, pivot);
        assert_eq!(result, solution);
    }
    for (nums, pivot, solution) in tests.clone() {
        let result = Solution3::pivot_array(nums, pivot);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
