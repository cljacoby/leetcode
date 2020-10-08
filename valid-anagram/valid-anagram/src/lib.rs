struct Solution;

use std::collections::HashMap;

/**
 *  First Solution
 * */
impl Solution {

    pub fn char_counts(s: &String) -> HashMap<char, u32> {
        let mut map = HashMap::with_capacity(s.len());
        for c in s.chars() {
            match map.get_mut(&c) {
                None => { map.insert(c, 1); },
                Some(num) => { *num += 1; },
            }
        }

        map
    }

    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map = Solution::char_counts(&s);
        let out = false;
        for c in t.chars() {
            match map.get_mut(&c) {
                None => { return false; },
                Some(num) => { *num -= 1; },
            }
        }

        map.iter()
            .map(|(c, num)| *num == 0)
            .fold(true, |acc, x| acc && x)
    }
}


/**
 *  Second Solution; Use Entry API
 * */

struct Solution2;

impl Solution2 {

    pub fn char_counts(s: &String) -> HashMap<char, u32> {
        let mut map = HashMap::new();
        for c in s.chars() {
            map.entry(c).and_modify(|num| *num += 1).or_insert(1);
        }

        map
    }

    pub fn is_anagram(s: String, t: String) -> bool {
        let s_map = Solution2::char_counts(&s);
        let t_map = Solution2::char_counts(&t);

        s_map == t_map
    }
}



#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_1() {
        let s = "anagram".to_string();
        let t = "naagram".to_string();
        let answer = true;
        assert_eq!(answer, Solution::is_anagram(s, t));
    }


    #[test]
    fn test_2() {
        let s = "rat".to_string();
        let t = "car".to_string();
        let answer = false;
        assert_eq!(answer, Solution::is_anagram(s, t));
    }

    #[test]
    fn test_3() {
        let s = "anagram".to_string();
        let t = "naagram".to_string();
        let answer = true;
        assert_eq!(answer, Solution2::is_anagram(s, t));
    }

    #[test]
    fn test_4() {
        let s = "anagram".to_string();
        let t = "naagram".to_string();
        let answer = true;
        assert_eq!(answer, Solution2::is_anagram(s, t));
    }

    // According to some guy on leetcode, my solution should cause
    // an overflow and this test shows it
    // #[test]
    fn test_5() -> Result<(), Box<std::error::Error>> {
        assert_eq!(
            false,
                Solution2::is_anagram(
                    String::from_utf8(vec![b'a';usize::from(u32::MAX as usize) * 2])?,
                    String::from_utf8(vec![b'a';usize::from(u32::MAX as usize) * 2])?,
                )
        );

        Ok(())
    }

}
