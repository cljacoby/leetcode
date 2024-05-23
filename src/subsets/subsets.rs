// https://leetcode.com/problems/subsets
struct Solution;

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut solutions = vec![vec![]];
        let mut path = vec![];
        Self::step(0, &nums, &mut path, &mut solutions);

        solutions
    }

    pub fn step(
        pre: usize,
        nums: &Vec<i32>,
        path: &mut Vec<i32>,
        solutions: &mut Vec<Vec<i32>>
    ) {
        for (i, num) in nums[pre..].iter().enumerate() {
            path.push(*num);
            solutions.push(path.clone());
            Self::step(pre + i + 1, nums, path, solutions);
            path.pop();
        }
    }
}

fn main() {
    let tests = vec![
        (
            vec![1, 2, 3],
            vec![
                vec![],
                vec![1],
                vec![2],
                vec![1, 2],
                vec![3],
                vec![1, 3],
                vec![2, 3],
                vec![1, 2, 3],
            ],
        ),
        (vec![0], vec![vec![], vec![0]]),
    ];

    for (nums, mut solution) in tests {
        let mut result = Solution::subsets(nums);
        let solution = solution.sort();
        let result = result.sort();
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
