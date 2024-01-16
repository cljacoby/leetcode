// https://leetcode.com/problems/insert-delete-getrandom-o1

use std::collections::HashMap;
use rand::rngs::ThreadRng;
use rand::seq::SliceRandom;

struct RandomizedSet {
    values: Vec<i32>,
    index: HashMap<i32, usize>,
    thread_rng: ThreadRng,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {
    fn new() -> Self {
        let values = vec![];
        let index = HashMap::new();
        let thread_rng = rand::thread_rng();

        Self { values, index, thread_rng }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if self.index.contains_key(&val) {
            return false;
        }

        self.index.insert(val, self.values.len());
        self.values.push(val);

        true
    }
    
    fn remove(&mut self, val: i32) -> bool {
        let idx = match self.index.get(&val) {
            None => return false,
            Some(idx) => *idx,
        };
        let last = self.values.last()
            .expect("Attempt to remove() while empty.")
            .to_owned();
        assert!(self.values.swap_remove(idx) == val);
        assert!(self.index.insert(last, idx).is_some());
        assert!(self.index.remove(&val).is_some());

        true
    }
    
    fn get_random(&mut self) -> i32 {
        self.values.as_slice()
            .choose(&mut self.thread_rng)
            .expect("Attempt to get_random() while empty")
            .to_owned()
    }

}

fn main() {
    let mut obj = RandomizedSet::new();
    assert!(obj.insert(1));
    assert!(obj.get_random() == 1);
    assert!(obj.remove(1));
    assert!(!obj.remove(2));

    assert!(obj.insert(0));
    assert!(obj.insert(1));
    assert!(obj.insert(2));
    for _ in 0..100 {
        let val = obj.get_random();
        assert!(val == 0 || val == 1 || val == 2)
    }

    assert!(obj.remove(1));
    assert!(!obj.remove(1));
    for _ in 0..100 {
        let val = obj.get_random();
        assert!(val == 0 || val == 2)
    }
    assert!(obj.remove(0));
    assert!(obj.remove(2));
 
    println!("✅ All tests passed");
}
