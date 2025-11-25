// https://leetcode.com/problems/power-of-two
struct Solution;

impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        let mut x: i32 = 1;
        if n >= 1 {
            while x <= i32::MAX {
                if x == n {
                    return true;
                }
                if let Some(v) = x.checked_mul(2) {
                    x = v;
                } else {
                    break;
                }
            }
            return false;
        }

        if n == 0 {
            return false;
        }

        while x >= i32::MIN {
            if x == n {
                return true;
            }
            if let Some(v) = x.checked_div(2) {
                x = v;
            } else {
                break;
            }
        }

        false
    }
}

fn main() {
    let tests = [
        (1, true),
        (16, true),
        (3, false),
    ];

    for (n, solution) in tests {
        let result = Solution::is_power_of_two(n);
        assert_eq!(result, solution, "failed n={:?}", n);
    }

    println!("✅ All tests passed")
}
