// https://leetcode.com/problems/score-of-a-string
struct Solution;

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let mut tot = 0;
        let bytes = s.as_bytes();
        for i in 1..bytes.len() {
            let a = bytes[i - 1] as i32;
            let b = bytes[i] as i32;
            tot += (a - b).abs();
        }

        tot
    }
}

fn main() {
    let tests = vec![
        ("hello".to_string(), 13),
        ("zaz".to_string(), 50),
    ];
    for (s, solution) in tests {
        let result = Solution::score_of_string(s);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
