// https://leetcode.com/problems/valid-palindrome
struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        println!("s = {:?}", s);
        let v: Vec<char> = s
            .chars()
            .filter(|c| c.is_alphanumeric())
            .map(|c| c.to_ascii_lowercase())
            .collect();

        let length = v.len();
        for i in 0..length {
            let j = length - i - 1;

            if i > j {
                return true;
            }

            println!("i={:?}, j={:?}, v[i]={:?}, v[j]={:?}", i, j, v[i], v[j]);

            if v[i] != v[j] {
                return false;
            }
        }

        return true;
    }
}

fn main() {
    let tests = vec![
        ("A man, a plan, a canal: Panama".to_string(), true),
        ("race a car".to_string(), false),
        ("racecar".to_string(), true),
        (" ".to_string(), true),
    ];

    for (s, solution) in tests.into_iter() {
        println!("*********************************");
        let result = Solution::is_palindrome(s);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
