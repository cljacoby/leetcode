// https://leetcode.com/problems/flatten-nested-list-iterator

#![allow(dead_code)]

#[derive(Debug, PartialEq, Eq)]
pub enum NestedInteger {
  Int(i32),
  List(Vec<NestedInteger>)
}

use std::collections::VecDeque;
#[derive(Debug)]
struct NestedIterator {
    next: Option<i32>,
    q: VecDeque<NestedInteger>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NestedIterator {
    fn new(list: Vec<NestedInteger>) -> Self {
        Self {
            q: VecDeque::from(list),
            next: None
        }
    }

    fn enque(&mut self) {
        if self.next.is_some() {
            return;
        }

        while let Some(x) = self.q.pop_front() {
            match x {
                NestedInteger::Int(x) => {
                    self.next = Some(x);
                    break;
                },
                NestedInteger::List(mut inner) => {
                    while let Some(y) = inner.pop() {
                        self.q.push_front(y);
                    }
                }
            }
        }
    }
    
    fn next(&mut self) -> i32 {
        assert!(self.next.is_some());
        let out = self.next.unwrap();
        self.next = None;
        self.enque();

        out
    }
    
    fn has_next(&mut self) -> bool {
        self.enque();
        self.next.is_some()
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * let obj = NestedIterator::new(nestedList);
 * let ret_1: i32 = obj.next();
 * let ret_2: bool = obj.has_next();
 */

fn main() {
    let tests = [
        (
            vec![
                NestedInteger::List(vec![NestedInteger::Int(1), NestedInteger::Int(1)]),
                NestedInteger::Int(2),
                NestedInteger::List(vec![NestedInteger::Int(1), NestedInteger::Int(1)]),
            ],
            vec![1, 1, 2, 1, 1],
        ),
        (
            vec![NestedInteger::List(vec![])],
            vec![],
        ),
    ];

    for (nums, solution) in tests {
        let mut iter = NestedIterator::new(nums);
        let mut idx = 0;
        while iter.has_next() {
            let next = iter.next();
            assert_eq!(next, solution[idx], "idx = {idx:?}, iter = {iter:?}");
            idx += 1;
        }
        assert_eq!(idx, solution.len());
    }
    println!("✅ All tests passed")
}
