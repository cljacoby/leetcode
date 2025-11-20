// https://leetcode.com/problems/zigzag-conversion
struct Solution;

use std::collections::VecDeque;

enum Op {
    Increment,
    Decrement,
}

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let n = num_rows as usize;
        let last = n - 1;
        let mut qs: VecDeque<VecDeque<char>> =
            VecDeque::from(vec![VecDeque::with_capacity(s.len()); n]);
        let mut idx = 0;
        let mut op = Op::Increment;

        let mut chars: VecDeque<char> = VecDeque::from_iter(s.chars());
        while let Some(ch) = chars.pop_front() {
            let q = qs.get_mut(idx).expect("idx went out of bounds");
            q.push_back(ch);

            if n == 1 {
                continue;
            }

            match op {
                Op::Increment => {
                    idx += 1;
                    if idx == last {
                        op = Op::Decrement;
                    }
                }
                Op::Decrement => {
                    idx -= 1;
                    if idx == 0 {
                        op = Op::Increment;
                    }
                }
            }
        }

        let mut out = String::with_capacity(s.len());
        while let Some(mut q) = qs.pop_front() {
            while let Some(ch) = q.pop_front() {
                out.push(ch);
            }
        }

        out
    }
}

fn main() {
    let tests = [
        (
            "PAYPALISHIRING".to_string(),
            3,
            "PAHNAPLSIIGYIR".to_string(),
        ),
        (
            "PAYPALISHIRING".to_string(),
            4,
            "PINALSIGYAHRPI".to_string(),
        ),
        (
            "PAYPALISHIRING".to_string(),
            1,
            "PAYPALISHIRING".to_string(),
        ),
    ];

    for (s, num_rows, solution) in tests {
        let result = Solution::convert(s, num_rows);
        assert_eq!(result, solution);
    }
}
