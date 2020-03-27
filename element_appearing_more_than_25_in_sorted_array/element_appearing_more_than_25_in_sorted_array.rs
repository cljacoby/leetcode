use std::collections::HashMap;

struct Solution;

impl Solution {

    pub fn get_counts(arr: &Vec<i32>) -> HashMap<i32, i32> {
        let mut counts = HashMap::new();
        for i in arr {
            match counts.get_mut(i) {
                Some(count) => { *count += 1; },
                None => { counts.insert(*i, 0); },
            }
        }

        counts
    }

    pub fn find_special_integer(arr: Vec<i32>) -> i32 {
        let counts = Solution::get_counts(&arr);
        let max_kv = counts.iter().max_by_key(|&(i, count)| count).unwrap();

        *max_kv.0
    }
}

fn main() {
    let  v = vec![1, 2, 2, 6, 6, 6, 6, 7, 10];
    let result = Solution::find_special_integer(v);
    println!("result = {:?}", result);
}

