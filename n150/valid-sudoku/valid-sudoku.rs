// https://leetcode.com/problems/valid-sudoku
struct Solution;

use std::collections::HashSet;

#[derive(Debug)]
struct SudokuCounter {
    pub rows: [HashSet<char>; 9],
    pub cols: [HashSet<char>; 9],
    pub sub_boxxes: [HashSet<char>; 9],
}

impl SudokuCounter {
    pub fn new() -> Self {
        let rows = std::array::from_fn(|_| HashSet::new());
        let cols = std::array::from_fn(|_| HashSet::new());
        let sub_boxxes = std::array::from_fn(|_| HashSet::new());

        Self {
            rows,
            cols,
            sub_boxxes,
        }
    }

    #[tracing::instrument(ret)]
    pub fn sub_box_index(i: usize, j: usize) -> usize {
        let x = i / 3;
        let y = j / 3;
        match (x, y) {
            (0, 0) => 0,
            (0, 1) => 1,
            (0, 2) => 2,
            (1, 0) => 3,
            (1, 1) => 4,
            (1, 2) => 5,
            (2, 0) => 6,
            (2, 1) => 7,
            (2, 2) => 8,
            _ => panic!("invalid sub_boxxes index, i={i}, j={j}, x={x}, y={y}"),
        }
    }
}

impl Solution {
    #[tracing::instrument(ret)]
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut counter = SudokuCounter::new();

        for (i, row) in board.iter().enumerate() {
            for (j, ch) in row.iter().enumerate() {
                if *ch == '.' {
                    continue;
                }

                let row_counter = counter.rows.get_mut(i).expect("invalid row index");
                if row_counter.contains(ch) {
                    return false;
                } else {
                    row_counter.insert(*ch);
                }

                let col_counter = counter.cols.get_mut(j).expect("invalid row index");
                if col_counter.contains(ch) {
                    return false;
                } else {
                    col_counter.insert(*ch);
                }

                let idx = SudokuCounter::sub_box_index(i, j);
                let sub_box_counter = counter.sub_boxxes.get_mut(idx).expect("invalid row index");
                if sub_box_counter.contains(ch) {
                    return false;
                } else {
                    sub_box_counter.insert(*ch);
                }
            }
        }

        true
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![
                vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
            ],
            true,
        ),
        (
            vec![
                vec!['8', '3', '.', '.', '7', '.', '.', '.', '.'],
                vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
            ],
            false,
        ),
    ];

    for (board, solution) in tests {
        let result = Solution::is_valid_sudoku(board);
        assert_eq!(result, solution);
    }

}
