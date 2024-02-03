// https://leetcode.com/problems/set-mismatch
struct Solution;

// Ugly. Should've just used a hashmap.

impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut arr = vec![0; nums.len()];
        let mut out: Vec<i32> = vec![-1, -1];
        for n in nums.iter() {
            arr[*n as usize - 1] += 1;
        }
        for n in 1..=nums.len() {
            if arr[n - 1] > 1 {
                out[0] = n as i32;
            } else if arr[n - 1] == 0 {
                out[1] = n as i32;
            }
            if out[0] != -1 && out[1] != -1 {
                break;
            }
        }

        out
    }
}

fn main() {
    let tests = vec![
        (vec![1, 2, 2, 4], vec![2, 3]),
        (vec![1, 1], vec![1, 2])
    ];

    for (nums, solution) in tests {
        let result = Solution::find_error_nums(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
