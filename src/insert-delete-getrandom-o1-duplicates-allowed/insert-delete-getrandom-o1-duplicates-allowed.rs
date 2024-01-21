// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed

use std::collections::HashMap;
use std::collections::HashSet;
use rand::rngs::ThreadRng;
use rand::seq::SliceRandom;

struct RandomizedCollection {
    values: Vec<i32>,
    // val -> (idx, count)
    index: HashMap<i32, HashSet<usize>>,
    thread_rng: ThreadRng,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedCollection {

    fn new() -> Self {
        let values = vec![];
        let index = HashMap::new();
        let thread_rng = rand::thread_rng();

        Self { values, index, thread_rng }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        match self.index.get_mut(&val) {
            Some(v) => {
                v.insert(self.values.len());
                self.values.push(val);
                false
            },
            None =>  {
                self.index.insert(val, HashSet::from([self.values.len()]));
                self.values.push(val);
                true
            }
        }
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if let Some(mut set)  = self.index.remove(&val) {
            let idx = set.iter().next()
                .expect("Empty index entry hashset")
                .to_owned();
            let last = self.values.last()
                .expect("Fail to get last");
            let last_set = self.index.get_mut(last)
                .expect("Fail to get last set");
            assert!(last_set.remove(&(self.values.len() - 1)));
            last_set.insert(idx);
            assert!(self.values.swap_remove(idx) == val);
            set.remove(&idx);
            if set.len() > 0 {
                assert!(self.index.insert(val, set).is_none());
            }

            return true;
        }

        false
    }
    
    fn get_random(&mut self) -> i32 {
        self.values.as_slice()
            .choose(&mut self.thread_rng)
            .expect("Attempt to get_random() while empty")
            .to_owned()
    }
}

fn main() {
    let mut obj = RandomizedCollection::new();
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
