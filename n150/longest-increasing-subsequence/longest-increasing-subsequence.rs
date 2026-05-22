// https://leetcode.com/problems/longest-increasing-subsequence
struct Solution;

impl Solution {

    #[tracing::instrument(ret)]
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![0; n + 1];
        dp[0] = 0;
        let mut max = 0;

        for (i, x) in nums.iter().enumerate() {
            let mut prev = 0;
            for (j, y) in nums[..i].iter().enumerate() {
                if y < x {
                    prev = i32::max(prev, dp[j+1]);
                }
            }
            dp[i+1] = prev + 1;
            max = i32::max(max, dp[i+1]);
            tracing::info!("i={i}, x={x}, dp={dp:?}, max={max}");
        }

        max
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![10,9,2,5,3,7,101,18],
            4,
        ),
        (
            vec![0,1,0,3,2,3],
            4,
        ),
        (
            vec![7,7,7,7,7,7,7],
            1,
        )
    ];


    for (nums, solution) in tests {
        let result = Solution::length_of_lis(nums);
        assert_eq!(result, solution);
    }
}
