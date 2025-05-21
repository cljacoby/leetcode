// https://leetcode.com/problems/set-matrix-zeroes
struct Solution;

use std::collections::HashSet;
use std::hash::Hash;

#[derive(Hash, PartialEq, Eq)]
enum Dimension {
    Row,
    Col,
}

impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
       let mut zeros = HashSet::<(Dimension, usize)>::new(); 
       let m = matrix.len();
       let n = matrix.get(0).expect("no rows").len();

       for (i, row) in matrix.iter().enumerate() {
           for (j, num) in row.iter().enumerate() {
               if *num == 0 {
                   zeros.insert((Dimension::Row, i));
                   zeros.insert((Dimension::Col, j));
               }
           }
       }

       for (dim, idx) in zeros.into_iter() {
           match dim {
               Dimension::Row => for j in 0..n {
                   *matrix.get_mut(idx).unwrap().get_mut(j).unwrap() = 0;
               },
               Dimension::Col => for i in 0..m {
                   *matrix.get_mut(i).unwrap().get_mut(idx).unwrap() = 0;
               }
           }
       }
    }
}

fn main() {
    let tests = vec![
        (
            vec![
                vec![0,1,2,0],
                vec![3,4,5,2],
                vec![1,3,1,5],
            ],
            vec![
                vec![0,0,0,0],
                vec![0,4,5,0],
                vec![0,3,1,0],
            ]
        ),
    ];

    for (mut matrix, solution) in tests.into_iter() {
        Solution::set_zeroes(&mut matrix);
        assert_eq!(matrix, solution);
    }

    println!("✅ All tests passed")
}
