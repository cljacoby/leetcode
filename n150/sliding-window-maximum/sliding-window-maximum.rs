// https://leetcode.com/problems/sliding-window-maximum
struct Solution;

use std::collections::{BinaryHeap, VecDeque, HashMap};

#[derive(Debug)]
struct WindowCounter {
    counts: HashMap<i32, usize>,
    pq: BinaryHeap<i32>, 
    max: i32,
}

impl WindowCounter {
    #[tracing::instrument]
    fn add(&mut self, x: i32) {
        self.counts.entry(x)
            .and_modify(|c| *c += 1)
            .or_insert(1);
        self.pq.push(x);
        let peek = self.pq.peek().expect("pq empty").to_owned();
        self.max = i32::max(self.max, peek);
    }

    #[tracing::instrument]
    fn remove(&mut self, x: i32) {
        *self.counts.get_mut(&x).expect("key not in counts") -= 1;
        if *self.counts.get(&x).unwrap() == 0 {
            self.counts.remove(&x).unwrap();
        }

        while let Some(peek) = self.pq.peek() && !self.counts.contains_key(&peek) {
            self.pq.pop().unwrap();
        }
        let peek = self.pq.peek().expect("pq empty").to_owned();
        self.max = peek;

    }
}

impl Solution {
    
    #[tracing::instrument(ret)]
    fn init_window_counter(window: &VecDeque<i32>) -> WindowCounter {
        let mut counts = HashMap::new();
        let mut pq = BinaryHeap::new();
        let mut max = i32::MIN;

        for num in window.iter() {
            counts.entry(*num)
                .and_modify(|c| *c += 1)
                .or_insert(1);
            pq.push(*num);
            max = i32::max(max, *num);
        }

        WindowCounter { counts, pq, max }
    }

    #[tracing::instrument(ret)]
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        assert!(k <= nums.len(), "k is larger than nums length");

        let mut window = VecDeque::from(nums);
        let mut nums = window.split_off(k);
        let mut counter = Self::init_window_counter(&window);
        let mut out = vec![counter.max];
        tracing::info!(out=?out, nums=?nums, counter=?counter, window=?window, "initialization");

        while let Some(num) = nums.pop_front() {
            window.push_back(num);
            counter.add(num);
            while window.len() > k {
                let rm = window.pop_front().expect("window empty");
                counter.remove(rm);
            }
            out.push(counter.max as i32);
            tracing::info!(num=?num, counter=?counter, window=?window, "finish iteration");
        }

        out
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![1,3,-1,-3,5,3,6,7],
            3,
            vec![3,3,5,5,6,7],
        ),
        (
            vec![1],
            1,
            vec![1],
        ),
        (
            vec![1,-1],
            1,
            vec![1, -1]
        ),
    ];

    for (nums, k, solution) in tests {
        let result = Solution::max_sliding_window(nums, k);
        assert_eq!(result, solution);
    }
}
