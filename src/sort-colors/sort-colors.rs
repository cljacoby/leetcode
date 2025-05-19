// https://leetcode.com/problems/sort-colors

use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut counts = HashMap::with_capacity(3);
        for num in nums.iter() {
            counts.entry(*num).and_modify(|c| *c += 1).or_insert(1);
        }

        let mut i = 0;
        for col in 0..3 {
            if let Some(count) = counts.get(&col) {
                for _ in 0..*count {
                    *nums.get_mut(i).unwrap() = col;
                    i += 1;
                }
            }
        }
    }
}

struct Solution1;
impl Solution1 {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut red = 0;
        let mut white = 0;
        let mut blue = nums.len() - 1;
        let mut i = 0;

        while white <= red {
            let x = nums.get(white).unwrap().to_owned();
            match x {
                // red
                0 => {
                    nums.swap(red, white);
                    red += 1;
                    white += 1;
                },
                // white
                1 => {
                    white += 1;
                },
                // blue
                2 => {
                    nums.swap(white, blue);
                    blue -= 1;
                },
                _ => panic!("color was not 0, 1, or 2")
            }
            i += 1;
        }
    }
}

fn main() {
    let tests = vec![
        (
            vec![2,0,2,1,1,0],
            vec![0,0,1,1,2,2],
        ),
        (
            vec![0],
            vec![0],
        )
    ];

    for (mut nums, solution) in tests.into_iter() {
        let mut nums1 = nums.clone();
        Solution::sort_colors(&mut nums1);
        assert_eq!(nums, solution);
        Solution1::sort_colors(&mut nums);
        assert_eq!(nums, solution);
    }
}
