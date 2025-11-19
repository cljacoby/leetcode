// https://leetcode.com/problems/1-bit-and-2-bit-characters
struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut q = VecDeque::from(bits);
        while let Some(bit) = q.pop_front() {
            match bit {
                0 => {
                    if q.is_empty() {
                        return true;
                    }
                }
                1 => {
                    let _ = q.pop_front().expect("1 cannot be last bit");
                }
                _ => panic!("problem statement guarantees 1 or 0"),
            }
        }

        false
    }
}

fn main() {
    let tests = [
        (vec![1, 0, 0], true),
        (vec![1, 1, 0], true),
        (vec![1, 1, 1, 0], false),
    ];

    for (bits, solution) in tests {
        let result = Solution::is_one_bit_character(bits);
        assert_eq!(result, solution);
    }
}
