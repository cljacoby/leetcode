// https://leetcode.com/problems/squares-of-a-sorted-array

struct Solution;

impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut neg = None;
        let split = nums.partition_point(|&x| x < 0);
        if split > 0 {
            neg = Some(split - 1);
        }
        let mut pos = split;
        let mut out = vec![];

        while neg.is_some() || pos < nums.len() {
            if let Some(n) = neg {
                if pos == nums.len() || -1 * nums[n] < nums[pos] {
                    out.push(nums[n].pow(2));
                    neg = n.checked_sub(1);
                    continue;
                }
            }
            out.push(nums[pos].pow(2));
            pos += 1;
        }

        out
    }
}

fn main() {
    let tests = vec![
        (vec![-4, -1, 0, 3, 10], vec![0, 1, 9, 16, 100]),
        (vec![-7, -3, 2, 3, 11], vec![4, 9, 9, 49, 121]),
        (vec![-4, -2, -1], vec![1, 4, 16]),
        (vec![1, 2, 4], vec![1, 4, 16]),
    ];

    for (nums, solution) in tests {
        let result = Solution::sorted_squares(nums);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
