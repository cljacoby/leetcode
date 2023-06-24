// https://leetcode.com/problems/reverse-bits
struct Solution;

impl Solution {
    fn bits_to_num(bits: &Vec<u32>) -> u32 {
        let mut n = 0;
        
        for (i, bit) in bits.iter().rev().enumerate() {
            let i = i as u32;
            n += bit * u32::pow(2, i);
        }

        n
    }

    pub fn reverse_bits(x: u32) -> u32 {
        let mut bits = vec![0; 32];
        
        for i in 0..32 {
            let i = i as u32;
            bits[i as usize] = x / u32::pow(2, i) % 2;
        }
        
        Solution::bits_to_num(&bits)
    }
}

fn main() {
    let tests = vec![
        (43261596, 964176192),
    ];

    for (input, output) in tests {
        let result = Solution::reverse_bits(input);
        assert_eq!(result, output);
    }
}
