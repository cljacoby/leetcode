// https://leetcode.com/problems/median-of-two-sorted-arrays
struct Solution;

use std::collections::VecDeque;

// O(m + n) solution
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut q1 = VecDeque::from(nums1);
        let mut q2 = VecDeque::from(nums2);
        let mut merged = Vec::with_capacity(q1.len() + q2.len());
        
        // println!("q1={q1:?}, q2={q2:?}");
        loop {
            match (q1.pop_front(), q2.pop_front()) {
                (None, None) => break,
                (Some(n1), None) => merged.push(n1),
                (None, Some(n2)) => merged.push(n2),
                (Some(n1), Some(n2)) => {
                    if n1 < n2 {
                        merged.push(n1);
                        q2.push_front(n2);
                    } else if n2 < n1 {
                        merged.push(n2);
                        q1.push_front(n1);
                    } else {
                        // n1 == n2
                        merged.extend([n1, n2]);
                    }
                },
            }
        }
        // println!("merged={merged:?}");
        
        let len = merged.len();
        let mid = len / 2;
        let out = if merged.len() % 2 == 0 {
            let a = *merged.get(mid - 1).unwrap();
            let b = *merged.get(mid).unwrap();
            (a + b) as f64 / 2.0
        } else {
            *merged.get(mid).unwrap() as f64
        };

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![1,3],
            vec![2],
            2.0f64
        ),
        (
            vec![1,2],
            vec![3,4],
            2.5f64
        ),
    ];

    for (n1, n2, solution) in tests {
        let result = Solution::find_median_sorted_arrays(n1, n2);
        assert_eq!(result, solution);
    }
}
