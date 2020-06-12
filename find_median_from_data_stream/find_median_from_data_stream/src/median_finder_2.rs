// Better solution using binary search tree

use crate::bst::{BST, BSTNode};

#[derive(Debug)]
struct MedianFinder {
    tree: BST<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    /** initialize your data structure here. */
    fn new() -> Self {
        Self {
            tree: BST::new(),
        }
    }
    
    fn add_num(&mut self, num: i32) {
        self.tree.insert(num);
    }
    
    fn find_median(&mut self) -> f64 {
        0 as f64
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

mod tests {

    use super::*;

    // #[test]
    // fn test_odd_num() {
    //     let v = vec![1, 2, 3, 4, 5];
    //     let mut median_finder = MedianFinder::new();
    //     for i in v {
    //         median_finder.add_num(i);
    //     }
    //     let median = median_finder.find_median();
    //     assert_eq!(median, 3 as f64);
    // }

    // #[test]
    // fn test_even_num() {
    //     let v = vec![1, 2, 3, 4, 5, 6];
    //     let mut median_finder = MedianFinder::new();
    //     for i in v {
    //         median_finder.add_num(i);
    //     }
    //     let median = median_finder.find_median();
    //     assert_eq!(median, 3.5);
    // }

    // #[test]
    // fn test_empty() {
    //     let mut median_finder = MedianFinder::new();
    //     let median = median_finder.find_median();
    //     assert_eq!(-1 as f64, median);
    // }

    // #[test]
    // fn test_one() {
    //     let mut median_finder = MedianFinder::new();
    //     median_finder.add_num(1);
    //     let median = median_finder.find_median();
    //     assert_eq!(1 as f64, median);
    // }


}