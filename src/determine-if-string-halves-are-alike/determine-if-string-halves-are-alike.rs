// https://leetcode.com/problems/determine-if-string-halves-are-alike
struct Solution;

impl Solution {
    pub fn count_vowels(s: &str) -> usize {
        let mut count = 0;

        for ch in s.chars() {
            if ch == 'a'
                || ch == 'e'
                || ch == 'i'
                || ch == 'o'
                || ch == 'u'
                || ch == 'A'
                || ch == 'E'
                || ch == 'I'
                || ch == 'o'
                || ch == 'U'
            {
                count += 1;
            }
        }

        count
    }

    pub fn halves_are_alike(s: String) -> bool {
        let mid = s.len() / 2;
        Self::count_vowels(&s[0..mid]) == Self::count_vowels(&s[mid..s.len()])
    }
}

fn main() {
    let tests = vec![("book".to_string(), true), ("textbook".to_string(), false)];
    for (s, solution) in tests {
        let result = Solution::halves_are_alike(s);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
