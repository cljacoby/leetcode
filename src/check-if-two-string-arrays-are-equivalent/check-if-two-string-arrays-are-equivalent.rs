// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

struct Solution;

impl Solution {
    pub fn array_strings_are_equal(w1: Vec<String>, w2: Vec<String>) -> bool {
        let w1: Vec<char> = w1.iter().flat_map(|s| s.chars()).collect();
        let w2: Vec<char> = w2.iter().flat_map(|s| s.chars()).collect();

        if w1.len() != w2.len() {
            return false;
        }

        for (a, b) in std::iter::zip(w1.iter(), w2.iter()) {
            if a != b {
                return false;
            }
        }

        true
    }
}

fn main() {
    let tests = [
        (
            vec!["ab".to_string(), "c".to_string()],
            vec!["a".to_string(), "bc".to_string()],
            true,
        ),
        (
            vec!["a".to_string(), "cb".to_string()],
            vec!["ab".to_string(), "c".to_string()],
            false,
        ),
    ];

    for (w1, w2, solution) in tests {
        let result = Solution::array_strings_are_equal(w1, w2);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
