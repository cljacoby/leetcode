use tracing_subscriber::EnvFilter;

// https://leetcode.com/problems/longest-palindromic-substring
struct Solution;

impl Solution {
    #[tracing::instrument(ret)]
    pub fn try_palindrome(s: &Vec<char>, mut i: usize, mut j: usize) -> Option<(usize, usize)> {
        let mut pal = None;
        while j < s.len() && s[i] == s[j] {
            pal = Some((i, j));
            i = match i.checked_sub(1) {
                None => break,
                Some(i) => i,
            };
            j += 1;
        }

        pal
    }

    #[tracing::instrument(ret)]
    pub fn longest_palindrome(s: String) -> String {
        assert!(s.len() > 0, "string is empty");
        assert!(s.is_ascii(), "string is not ascii");

        let s: Vec<char> = s.chars().collect();
        let mut mxpal = (0, 0);
        for i in 0..s.len() {
            if let Some(pal) = Self::try_palindrome(&s, i, i) {
                if pal.1 - pal.0 > mxpal.1 - mxpal.0 {
                    mxpal = pal;
                }
            }
            if let Some(pal) = Self::try_palindrome(&s, i, i + 1) {
                if pal.1 - pal.0 > mxpal.1 - mxpal.0 {
                    mxpal = pal;
                }
            }
        }

        s[mxpal.0..=mxpal.1].iter().collect()
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            "babad".to_string(),
            "bab".to_string(),
        ),
        (
            "cbbd".to_string(),
            "bb".to_string(),
        ),
        (
            "bb".to_string(),
            "bb".to_string(),
        ),
        (
            "ccc".to_string(),
            "ccc".to_string(),
        ),
        (
            "ccd".to_string(),
            "cc".to_string(),
        ),
        (
            "aaaa".to_string(),
            "aaaa".to_string(),
        ),
    ];

    for (s, solution) in tests {
        let result = Solution::longest_palindrome(s);
        assert_eq!(result, solution);
    }
}
