// https://leetcode.com/problems/reverse-bits
struct Solution;

/** 
 * Note to self, I should probably be able to do this with bit shifts
 * instead of the array, but I don't use bit shifting often enough to
 * be readily able to use the << / >> operations.
 * */

impl Solution {
    const SIZE: usize = 32;

    fn sbits(bits: &[u8; Self::SIZE]) -> String {
        let mut s = String::with_capacity(bits.len() + 4);
        for (i, bit) in bits.iter().enumerate() {
            if i != 0 && i % 8 == 0 {
                s.push('-');
            }
            s.push_str(&format!("{}", bit));
        }

        s
    }
    
    fn i32_to_bits(n: i32) -> [u8; Self::SIZE] {
        let mut x = n;
        let mut bits = [0; Self::SIZE];
        let mut i = Self::SIZE - 1;

        while x > 0 && i > 0 {
            let rem = x % 2;
            x -= rem;
            x /= 2;
            bits[i] = rem as u8;
            i -= 1;
        }

        bits
    }

    fn bits_to_i32(bits: [u8; Self::SIZE]) -> i32 {
        let mut tot = 0;
        for i in (1..=30).rev() {
            let bit = bits[i];
            let pow = (30 - i + 1) as u32;
            tot += bit as i32 * i32::pow(2, pow);
            tracing::info!(i=?i, bit=?bit, pow=?pow, tot=?tot, bits=?Self::sbits(&bits), "bits_to_i32");
        }

        tot
    }

    pub fn reverse_bits(n: i32) -> i32 {
        assert!(n >= 0 && n <= 2147483646, "n is outside of range (0, 2147483646]");
        assert!(n % 2 == 0, "n is odd");
        
        let mut bits = Self::i32_to_bits(n);
        tracing::info!(n=?n, bits=?Self::sbits(&bits), "input to bits");
        bits.reverse();
        tracing::info!(bits=?Self::sbits(&bits), "bits reversed");
        let out = Self::bits_to_i32(bits);
        tracing::info!(out=?out, "out");

        out
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (0, 0),
        (10, 1342177280),
        (2147483646, 2147483646),
        (43261596, 964176192),
        (2147483644, 1073741822),
    ];

    for (x, solution) in tests {
        let result = Solution::reverse_bits(x);
        assert_eq!(result, solution);
    }
}
