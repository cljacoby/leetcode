// https://leetcode.com/problems/longest-common-subsequence
struct Solution;

use std::collections::HashMap;

/*
 * Ugh, had this one 99% of the way there, and got derailed on a tiny detail.
 * Originally, I was trying to pass down a `length` variable down the recursions,
 * and update it accordingly. Then when a bounds violation was observed it would return
 * the last value of `length` back up the call stack, and it would use i32::max to pick.
 * The right value.
 *
 * This worked without caching, but with caching it would get the wrong answer. I'm still not
 * really sure why it can't work that way; however, the fix was instead to return 0 when a bounds
 * check was observed, and then as we move back up the call stack we add 1 to the return value
 * at each recursion call.
 *
 * Key insight: 
 * Add 1 upon the recrusive call's return, not in the argument value.
 * */

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let s1 = text1.chars().collect::<Vec<char>>();
        let s2 = text2.chars().collect::<Vec<char>>();
        let mut cache = HashMap::new();
        
        Solution::step(&s1, &s2, 0, 0, &mut cache) as i32
    }

    fn step(
        s1: &Vec<char>,
        s2: &Vec<char>,
        i: usize,
        j: usize,
        cache: &mut HashMap<(usize, usize), usize>,
    ) -> usize {
        // println!("enter step() i={i}, j={j}");
        if i >= s1.len() ||
            j >= s2.len()
        {
            return 0;
        }

        if let Some(n) = cache.get(&(i, j)) {
            return *n;
        }

        
        let n = if s1[i] == s2[j] {
            1 + Solution::step(s1, s2, i + 1, j + 1, cache)
        }
        else {
            usize::max(
                Solution::step(s1, s2, i + 1, j, cache),
                Solution::step(s1, s2, i, j + 1, cache)
            )
        };
        cache.insert((i, j), n);

        n
    }
}

fn main() {
    let tests = vec![
        ("abcde".to_string(), "ace".to_string(), 3),
        ("abc".to_string(), "abc".to_string(), 3),
        ("abc".to_string(), "def".to_string(), 0),
        ("bl".to_string(), "yby".to_string(), 1),
        ("pmjghexybyrgzczy".to_string(), "hafcdqbgncrcbihkd".to_string(), 4),
    ];

    for (s1, s2, solution) in tests {
        println!("******************************");
        println!("Start s1={s1}, s2={s2}");
        let result = Solution::longest_common_subsequence(s1.clone(), s2.clone());
        assert_eq!(result, solution);
    }
    println!("✅ All tests passed")
}

