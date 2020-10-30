struct Solution;

use std::collections::HashSet;
use std::collections::HashMap;

/*
 * This solution probably makes a lot of redundant memory allocations, but
 * it was a fun way to try out the labeled loop syntax.
 * */

impl Solution {

    pub fn char_counts(s: &String) -> HashMap<char, u32> {
        let mut map = HashMap::new();
        for c in s.chars() {
            map.entry(c).and_modify(|i| *i += 1).or_insert(1);
        }

        map
    }

    pub fn common_chars(mut a: Vec<String>) -> Vec<String> {
       let maps: Vec<HashMap<char, u32>> = a.iter()
           .map(|s| Solution::char_counts(s))
           .collect();

       let char_set: HashSet<char> = a.iter()
           .map(|s| s.chars())
           .flatten()
           .collect();

       let mut out: Vec<String> = vec![]; 

       let mut iterchars = char_set.iter();
       'outer: loop {
           if let Some(c) = iterchars.next() {
               let mut lowest = u32::MAX;
               for map in maps.iter() {
                    lowest = match map.get(&c) {
                        None => continue 'outer,
                        Some(count) => if lowest < *count { lowest } else { *count },
                    };
               }
               for _ in 0..lowest {
                   out.push(c.to_string());
               }
           } else {
               // Iterator exhausted
                break 'outer;
           }
       }
    
        out
    }

}

#[cfg(test)]
mod tests {

    use super::Solution;

    #[test]
    fn test_char_counts() {
        let s = "cardigan".to_string();
        let map = Solution::char_counts(&s);
        println!("map = {:?}", map);
    }

    /*
     * NOTE:
     * The leetcode problem statement says the answer may be returned in any
     * order; however, the template function signature uses a Vec<String>. In
     * */

    #[test]
    fn test_1() {
        let words = vec![
            "bella".to_string(),
            "label".to_string(),
            "roller".to_string(),
        ];
        let result = Solution::common_chars(words);
        assert_eq!(result, ["e", "l", "l"]);
    }

    #[test]
    fn test_2() {
        let words = vec![
            "cool".to_string(),
            "lock".to_string(),
            "cook".to_string(),
        ];
        let result = Solution::common_chars(words);
        assert_eq!(result, ["c", "o"]);
    }
}
