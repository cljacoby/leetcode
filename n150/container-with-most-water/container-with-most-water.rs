// https://leetcode.com/problems/container-with-most-water
struct Solution;

impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = heights.len() - 1;
        let mut max = i32::MIN;

        while i < j {
            let h1 = heights[i];
            let h2 = heights[j];
            let h = i32::min(h1, h2);
            let area = h * (j - i) as i32;
            max = i32::max(max, area);
            if h1 > h2 {
                j -= 1;
            } else {
                i += 1;
            }
        }

        max
    }
}

fn main() {
    let tests = vec![
        (
            vec![1,8,6,2,5,4,8,3,7],
            49,
        ),
        (
            vec![1,7,6,2,5,4,8,3,7],
            49,
        ),
        (
            vec![1,1],
            1,
        ),
    ];

    for (heights, solution) in tests {
        let result = Solution::max_area(heights);
        assert_eq!(result, solution);
    }

}
