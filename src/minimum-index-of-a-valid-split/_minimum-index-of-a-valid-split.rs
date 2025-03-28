
// https://leetcode.com/problems/minimum-index-of-a-valid-split
struct Solution;

use std::collections::HashMap;
use std::hash::Hash;

#[derive(Debug)]
struct Counter<T: Hash + Eq + Clone> {
    map: HashMap<T, usize>,
    max: Option<T>
}

impl<T: Hash + Eq + Clone> Counter<T> {
    fn new() -> Self {
        let map = HashMap::new();
        let max = None;

        Self { map, max }
    }

    fn incr(&mut self, key: &T) {
        if let Some(c) = self.map.get_mut(key) {
            *c += 1
        } else {
            self.map.insert(key.clone(), 1);
        }

        if let Some(max) = &self.max {
            if self.map[&max] < self.map[key] {
                self.max = Some(key.clone())
            }
        } else {
            self.max = Some(key.clone())
        }
    }

    fn decr(&mut self, key: &T) {
        if let Some(c) = self.map.get_mut(key) {
            *c = c.saturating_sub(1);
        }
        if let Some(max) = &self.max {
            if max == key {
                let (k, _v) = self.map
                    .iter()
                    .max_by_key(|(_k, v)| *v)
                    .unwrap();
                self.max = Some(k.clone());
            }
        }
    }

    fn max(&self) -> Option<&T> {
        self.max.as_ref()
    }
}

impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let mut r: Vec<i32> = nums.into_iter().rev().collect();
        let mut l = vec![];
        let mut rc = Counter::new();
        let mut lc = Counter::new();
        for num in r.iter() {
            rc.incr(num);
        }

        while let Some(num) = r.pop() {
            rc.decr(&num);
            lc.incr(&num);
            l.push(num);
            println!("l = {:?}\n    r = {:?}\n    lc={:?}\n    rc={:?}", l, r, lc, rc);

            match (rc.max(), lc.max()) {
                (Some(rmax), Some(lmax)) => {
                    if rmax == lmax
                        && rc.map[rmax] > r.len() / 2
                        && lc.map[lmax] > l.len() / 2
                    {
                        return (l.len() - 1) as i32
                    }
                },
                _ => continue
            }
        }

        -1
    }
}

fn main() {
    let tests = vec![
        (vec![1,2,2,2], 2),
        (vec![2,1,3,1,1,1,7,1,2,1], 4),
    ];

    for (nums, solution) in tests.into_iter() {
        let result = Solution::minimum_index(nums);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
