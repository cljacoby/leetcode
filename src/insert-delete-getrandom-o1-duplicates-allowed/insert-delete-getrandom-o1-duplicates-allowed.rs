// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed

use std::collections::HashMap;
use std::collections::HashSet;
use rand::rngs::ThreadRng;
use rand::seq::SliceRandom;

#[derive(Debug)]
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
            Some(hset) => {
                assert!(hset.insert(self.values.len()));
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

    fn val_idx_pop_next(&self, val: &i32) -> Option<usize> {
        if let Some(hset) = self.index.get(val) {
            let idx = hset.iter().next()
                .expect("Hset present with no indices")
                .to_owned();

            return Some(idx);
        }

        None
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if let None = self.index.get(&val) {
            return false;
        }

        let idx = self.val_idx_pop_next(&val)
            .expect("Index had val entry, but did not get index to pop");
        let last = self.values.last()
            .expect("Fail to get last")
            .to_owned();
        let last_hset = self.index.get_mut(&last)
            .expect("Fail to get last set");
        assert!(last_hset.remove(&(self.values.len() - 1)));
        last_hset.insert(idx);
        assert!(self.values.swap_remove(idx) == val);

        let hset = self.index.get_mut(&val)
            .expect("Did not get hset for val");
        hset.remove(&idx);

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
    let mut obj = RandomizedCollection::new();
    assert!(obj.insert(1));
    println!("obj = {:?}", obj);
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
