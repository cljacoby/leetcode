// https://leetcode.com/problems/reverse-prefix-of-word
struct Solution;

impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        match word.split_once(ch) {
            Some((left, right)) => {
                // split_once() has the effect of removing the split character.
                // Since we're reversing the substring, push the split char first.
                let mut s = String::from(ch);
                s.extend(left.chars().rev());
                s.push_str(right);
                
                s
            },
            None => {
                word
            }
        }
    }
}

fn main() {
    let tests = vec![
        ("abcdefd".to_string(), 'd', "dcbaefd".to_string()),
        ("xyxzxe".to_string(), 'z', "zxyxxe".to_string()),
        ("abcd".to_string(), 'z', "abcd".to_string())
    ];
    for (word, ch, solution) in tests {
        let result = Solution::reverse_prefix(word, ch);
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}
