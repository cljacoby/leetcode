struct Solution;

impl Solution {
    pub fn hamming_weight (n: u32) -> i32 {
        n.count_ones() as i32
    }
}

fn main() {
    let tests = vec![
        (11, 3),
        (128, 1),
        (4294967293, 31),
    ];


    for (n, solution) in tests {
        let result = Solution::hamming_weight(n);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
