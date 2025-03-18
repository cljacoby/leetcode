// https://leetcode.com/problems/longest-nice-subarray
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let nums: Vec<u32> = nums
            .into_iter()
            .map(|i| i.try_into().expect("not positive int"))
            .collect();
        let mut win: VecDeque<u32> = VecDeque::with_capacity(nums.len());
        let mut max = 0;

        for x in nums.into_iter() {
            let drain = 'inner: {
                for (i, y) in win.iter().enumerate().rev() {
                    if x & y != 0 {
                        break 'inner Some(i);
                    }
                }
                None
            };

            if let Some(idx) = drain {
                win.drain(..=idx);
            }

            win.push_back(x);
            max = i32::max(max, win.len() as i32);
        }

        max
    }
}

fn main() {
    let tests = vec![
        (vec![1, 3, 8, 48, 10], 3),
        (vec![3, 1, 5, 11, 13], 1),
        (
            vec![
                84139415, 693324769, 614626365, 497710833, 615598711, 264, 65552, 50331652, 1,
                1048576, 16384, 544, 270532608, 151813349, 221976871, 678178917, 845710321,
                751376227, 331656525, 739558112, 267703680,
            ],
            8,
        ),
    ];

    for (nums, solution) in tests.into_iter() {
        println!("*********************");
        let result = Solution::longest_nice_subarray(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
