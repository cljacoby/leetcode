// https://leetcode.com/problems/remove-all-occurrences-of-a-substring
struct Solution;

impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        let mut out = Vec::new();
        let part: Vec<char> = part.chars().collect();
        let sz = part.len();

        for ch in s.chars() {
            out.push(ch);
            if let Some(offset) = out.len().checked_sub(sz) {
                if &out[offset..] == &part {
                    out.truncate(offset);
                }
            }
        }

        out.into_iter().collect()
    }
}

fn main() {
    let tests = vec![
        ("daabcbaabcbc".to_string(), "abc".to_string(), "dab".to_string()),
        ("axxxxyyyyb".to_string(), "xy".to_string(), "ab".to_string()),
    ];

    for (s, part, solution) in tests {
        let result = Solution::remove_occurrences(s, part);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
