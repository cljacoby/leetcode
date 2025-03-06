// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut nums1 = VecDeque::from(nums1);
        let mut nums2 = VecDeque::from(nums2);
        let mut out = Vec::with_capacity(nums1.len() + nums2.len());

        loop {
            match (nums1.pop_front(), nums2.pop_front()) {
                (Some(mut n1), Some(n2)) => {
                    if n1[0] == n2[0] {
                        n1[1] += n2[1];
                        out.push(n1);
                    } else if n1[0] < n2[0] {
                        out.push(n1);
                        nums2.push_front(n2);
                    } else {
                        out.push(n2);
                        nums1.push_front(n1);
                    }
                },
                (None, Some(n2)) => out.push(n2),
                (Some(n1), None) => out.push(n1),
                (None, None) => break,
            }
        }

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![vec![1,2],vec![2,3],vec![4,5]],
            vec![vec![1,4],vec![3,2],vec![4,1]],
            vec![vec![1,6],vec![2,3],vec![3,2],vec![4,6]]
        ),
    ];

    for (nums1, nums2, solution) in tests {
        let result = Solution::merge_arrays(nums1, nums2);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
