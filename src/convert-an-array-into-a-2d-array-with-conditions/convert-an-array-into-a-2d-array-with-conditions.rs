// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let len = nums.len();
        let mut counts = HashMap::with_capacity(len);
        for num in nums.iter() {
            *counts.entry(*num).or_insert(0) += 1;
        }

        let mut rows = vec![];
        while counts.len() > 0 {
            rows.push(vec![]);
            let idx = rows.len() - 1;
            for (num, count) in counts.iter_mut() {
                rows[idx].push(*num);
                *count -= 1;
            }
            counts.retain(|_, &mut v| v > 0);
        }

        rows
    }
}


// Leetcode uses Vecs; however, since HashMap iteration order isn't consistent, need
// to convert to HashSets to do a meaninful correctness test.
use std::collections::HashSet;
fn vec_to_set(arr: Vec<Vec<i32>>) -> Vec<HashSet<i32>> {
    arr.into_iter()
        .map(|inner| inner.into_iter().collect())
        .collect()
}

fn main() {
    let tests = vec![
        (
            vec![1, 3, 4, 1, 2, 3, 1],
            vec![vec![1, 3, 4, 2], vec![1, 3], vec![1]],
        ),
        (
            vec![1, 2, 3, 4],
            vec![vec![4, 3, 2, 1]]),
    ];

    for (nums, solution) in tests {
        let result = Solution::find_matrix(nums);
        let r = vec_to_set(result);
        let s = vec_to_set(solution);
        assert_eq!(r, s);
    }

    println!("✅ All tests passed")
}
