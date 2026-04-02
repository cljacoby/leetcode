// https://leetcode.com/problems/reverse-integer
struct Solution;

impl Solution {
    #[tracing::instrument(ret)]
    pub fn reverse(x: i32) -> i32 {
        Self::try_reverse(x).unwrap_or(0)
    }

    #[tracing::instrument(ret)]
    pub fn try_reverse(x: i32) -> Option<i32> {
        let negative = x < 0;
        let mut rem = i32::checked_abs(x).or_else(|| {
            tracing::info!(x=x, "i32 overflow on abs");
            None
        })?;
        let mut digits = Vec::with_capacity(10);

        while rem > 0 {
            let digit = rem % 10;
            digits.push(digit);
            rem /= 10;
            tracing::info!(digit=?digit, digits=?digits, "mod loop");
        }

        let mut exp = 0;
        let mut tot: i32 = 0;
        while let Some(digit) = digits.pop() {
            let mag = i32::checked_pow(10, exp).or_else(|| {
                tracing::info!(x=x, digit=digit, "i32 overflow on exponentiation");
                None
            })?;
            let add = digit.checked_mul(mag).or_else(|| {
                tracing::info!(x=x, digit=digit,  "i32 overflow on multiply");
                None
            })?;
            tot = tot.checked_add(add).or_else(|| {
                tracing::info!(x=x, digit=digit,  "i32 overflow on add");
                None
            })?;
            tracing::info!(digit=digit, exp=exp, add=add, tot=tot, "add loop");
            exp += 1;
        }

        if negative {
            tot = tot.checked_mul(-1).or_else(|| {
                tracing::info!(x=x, tot=tot,  "i32 overflow on inverting sign");
                None
            })?;
        }

        Some(tot)
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (123, 321),
        (-123, -321),
        (0, 0),
        (120, 21),
        (i32::MAX, 0),
        (i32::MIN, 0),
    ];

    for (x, solution) in tests {
        let result = Solution::reverse(x);
        assert_eq!(result, solution);
    }

}
