#![feature(get_many_mut)]

// https://leetcode.com/problems/apply-operations-to-an-array
struct Solution;
impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        let mut i = 0;
        while let Ok([a, b]) = nums.get_many_mut([i, i+1]) {
            if a == b {
                *a *= 2;
                *b = 0;
                i += 2;
            } else {
                i += 1;
            }
        }

        let mut out = Vec::with_capacity(nums.len());
        let mut zeros = 0;
        for num in nums.into_iter() {
            if num == 0 {
                zeros += 1;
            } else {
                out.push(num);
            }
        }
        out.extend(vec![0; zeros]);

        out
    }
}

// Leetcode doesn't allow nightly feature flags.
struct Solution2;
impl Solution2 {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        let mut i = 0;
        let length = nums.len();
        let end = length.saturating_sub(1);
        while i < end {
            if nums[i] == nums[i+1] {
                nums[i] *= 2;
                nums[i+1] = 0;
                i += 2;
            } else {
                i += 1;
            }
        }

        let mut out: Vec<i32> = nums.into_iter().filter(|x| *x != 0).collect();
        out.resize(length, 0);

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![1,2,2,1,1,0],
            vec![1,4,2,0,0,0]
        ),
        (
            vec![0,1],
            vec![1,0],
        ),
    ];

    for (nums, solution) in tests.clone() {
        let result = Solution::apply_operations(nums);
        assert_eq!(result, solution);
    }
    
    for (nums, solution) in tests {
        let result = Solution2::apply_operations(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
