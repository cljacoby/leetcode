/**
 *  Solution strategy:
 *  * Sort Vec<String> to length order descending
 *  * Take the shortest String (0th element)
 *  * Check that every other string in the Vec has a prefix matching shortest string
 *  * return
 * */
use std::collections::HashMap;

struct Solution;
type Sol = Solution;

impl Solution {
    pub fn char_vec(s: &String) -> Vec<char> {
        let char_vec: Vec<char> = s.clone().chars().collect();

        char_vec
    }

    pub fn char_index_map(s: &String) -> HashMap<usize, char> {
        let char_index_map: HashMap<usize, char> = s.char_indices().collect();

        char_index_map
    }

    pub fn longest_common_prefix(mut strs: Vec<String>) -> String {
        // Initialize output variable
        let mut s = String::from("");

        // Assess early return if strs is empty
        if strs.len() == 0 {
            return s;
        }

        // Get shortest String, and pop from Vec. Create char index map for shortest.
        let (i, _) = strs
            .iter()
            .enumerate()
            .min_by_key(|(i, s)| s.len())
            .unwrap();
        let shortest = strs.remove(i);
        let shortest_map = Sol::char_index_map(&shortest);

        // Create character mapping for each remaining String in strs
        let strs_maps: Vec<HashMap<usize, char>> =
            strs.iter().map(|s| Sol::char_index_map(s)).collect();

        // Iterate over remaining strs, and see if they're characters match shortest
        for i in 0..shortest.len() {
            let c = shortest_map.get(&i).unwrap();
            for strs_map in strs_maps.iter() {
                let c2 = strs_map.get(&i).unwrap();
                if c != c2 {
                    return s;
                }
            }
            s.push(*c);
        }

        s
    }
}

fn main() {}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_positive() {
        let lcp = Solution::longest_common_prefix(vec![
            "flower".to_string(),
            "flow".to_string(),
            "flight".to_string(),
        ]);
        println!("lcp = {:?}", lcp);
        assert_eq!(lcp, "fl".to_string());
    }

    #[test]
    fn test_negative() {
        let lcp2 = Solution::longest_common_prefix(vec![
            "dog".to_string(),
            "racecar".to_string(),
            "car".to_string(),
        ]);
        println!("lcp2 = {:?}", lcp2);
        assert_eq!(lcp2, "".to_string());
    }
}
