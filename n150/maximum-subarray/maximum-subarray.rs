// https://leetcode.com/problems/maximum-subarray
struct Solution;

impl Solution {

    #[tracing::instrument(ret)]
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut dp = vec![0; nums.len() + 1];
        dp[0] = 0;

        for i in 1..=nums.len() {
            let num = nums.get(i - 1).expect("fail to index into nums");
            let val = i32::max(*num, *num + dp[i - 1]);
            dp[i] = val;
        }
        tracing::info!(dp=?dp, "recurrance table");

        let mut max = i32::MIN;

        // note: edge case here of whether an empty slice is considered a valid sub-array.
        // it appears this leetcode quesion deems the answer to be 'no'
        for num in &dp[1..] {
            max = i32::max(max, *num);
        }
        tracing::info!(max=?max, "max");

        max
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![-2,1,-3,4,-1,2,1,-5,4],
            6,
        ),
        (
            vec![5,4,-1,7,8],
            23,
        ),
        (
            vec![1],
            1,
        ),
        (
            vec![-1],
            -1,
        ),
    ];

    for (nums, solution) in tests {
        let result = Solution::max_sub_array(nums);
        assert_eq!(result, solution);
    }
}
