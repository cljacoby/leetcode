// https://leetcode.com/problems/daily-temperatures
struct Solution;

impl Solution {
    pub fn daily_temperatures(temps: Vec<i32>) -> Vec<i32> {
        let mut out: Vec<i32> = vec![0; temps.len()];
        let mut stack: Vec<(usize, i32)> = vec![];

        for (i, t1) in temps.iter().enumerate() {
            while let Some(tup) = stack.last() {
                let (j, t2) = tup.to_owned();
                if t2 >= *t1 {
                    break;
                }
                out[j] = (i - j) as i32;
                stack.pop();
            }
            stack.push((i, *t1));
        }

        out
    }
}

fn main() {
    let tests = vec![
        (
            vec![73, 74, 75, 71, 69, 72, 76, 73],
            vec![1, 1, 4, 2, 1, 1, 0, 0],
        ),
        (
                vec![30,40,50,60],
                vec![1,1,1,0],
        ),
        (
            vec![30,60,90],
            vec![1,1,0],
        )
    ];

    for (temps, solution) in tests {
        let result = Solution::daily_temperatures(temps);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
