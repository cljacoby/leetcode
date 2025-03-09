// https://leetcode.com/problems/alternating-groups-i
struct Solution;

pub fn next(i: usize, len: usize) -> usize {
    (i + 1) % len
}

impl Solution {


    pub fn number_of_alternating_groups(colors: Vec<i32>) -> i32 {
        let len = colors.len();
        let mut i = 0;
        let mut j = 2;
        let mut count = 0;


        loop {
            if colors[i] == colors[j]
                && colors[i] != colors[next(i, len)]
            {
                count += 1;
            }

            i = next(i, len);
            j = next(j, len);

            if i == 0 {
                break;
            }
        }

        count
    }
}

fn main() {
    let tests = vec![
        (vec![1,1,1], 0),
        (vec![0,1,0,0,1], 3),
    ];

    for (colors, solution) in tests.into_iter() {
        let result = Solution::number_of_alternating_groups(colors);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
