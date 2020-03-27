use std::collections::HashSet;
use std::iter::FromIterator;

struct Solution;

impl Solution {
    pub fn letters() -> HashSet<char> {
        let letters: HashSet<char> = vec![
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]
        .into_iter()
        .collect();

        letters
    }

    pub fn word_to_char_set(word: &String) -> HashSet<char> {
        let letters = Solution::letters();
        let mut char_set: HashSet<char> = HashSet::new();

        word.clone()
            .chars()
            .filter(|c| !c.is_whitespace())
            .map(|c| c.to_ascii_lowercase())
            .filter(|c| letters.get(c).is_some())
            .map(|c| {
                char_set.insert(c);
                c
            })
            .count();

        char_set
    }

    pub fn shortest_completing_word(license_plate: String, words: Vec<String>) -> String {
        let lp_char_set = Solution::word_to_char_set(&license_plate);
        let mut opts = Vec::new();

        for word in words.iter() {
            let char_set = Solution::word_to_char_set(word);
            let diff: Vec<&char> = lp_char_set.difference(&char_set).collect();
            if diff.len() == 0 {
                opts.push(word);
            }
        }

        let shortest = opts.get(0).unwrap();
        for opt in opts.iter().rev() {
            if opt.len() < shortest.len() {
                let shortest = opt;
            }
        }

        println!("shortest = {:?}", shortest);

        (*shortest).to_string()
    }
}

fn main() {
    println!("Hello, world!");
}

mod tests {

    use super::*;

    #[test]
    fn test_solution() {
        let result = Solution::shortest_completing_word(
            "1s3 PSt".to_string(),
            vec![
                "step".to_string(),
                "steps".to_string(),
                "stripe".to_string(),
                "stepple".to_string(),
            ],
        );
    }

    #[test]
    fn test_word_to_char_set() {
        let word = "1s3 PSt".to_string();
        let char_set = Solution::word_to_char_set(&word);
        println!("char_set = {:?}", char_set);

        let control: HashSet<char> = vec!['s', 'p', 's', 't'].into_iter().collect();
        let diff1: Vec<&char> = char_set.difference(&control).collect();
        let diff2: Vec<&char> = control.difference(&char_set).collect();

        assert!(diff1.len() == 0 && diff2.len() == 0);
    }
}
