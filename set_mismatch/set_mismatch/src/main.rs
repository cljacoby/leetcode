struct Solution;

/**
 * Solution:
 * - Loop through numbers
 * - Place in HashMap with number hashed to count
 * - Identify repeat in loop
 * - Identify max in loop
 * */

// *******************************
// *******************************

type Sol = Solution;

use std::collections::HashMap;

impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut map: HashMap<i32, i32> =
            HashMap::with_capacity(nums.len() as usize);
        let mut mis = -1;
        let mut dup = -1;
        for num in nums.iter() {
            map.entry(*num)
                .and_modify(|v| *v += 1)
                .or_insert(1);
        }
        for i in 1..= (nums.len() as i32) {
            if map.get(&i).is_some() {
                if *map.get(&i).unwrap() == 2 {
                    dup = i;
                }
            } else {
                mis = i;
            }
        }

        vec![dup, mis]
    
    }
}

fn main() {
    let sol = Sol::find_error_nums(vec![1, 2, 2, 4]);
    println!("sol = {:#?}", sol);
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_1() {
        let sol = Sol::find_error_nums(vec![1, 2, 2, 4]);
        assert_eq!(sol, vec![2, 3]);
    }

    #[test]
    fn test_2() {
        let sol = Sol::find_error_nums(vec![1, 1]);
        assert_eq!(sol, vec![1, 2]);
    }
}
