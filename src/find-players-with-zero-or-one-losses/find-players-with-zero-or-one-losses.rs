// https://leetcode.com/problems/find-players-with-zero-or-one-losses
struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut score = HashMap::new();
        let mut a = vec![];
        let mut b = vec![];

        for pair in matches {
            score.entry(pair[0]).or_insert((0, 0)).0 += 1;
            score.entry(pair[1]).or_insert((0, 0)).1 += 1;
        }

        for (id, (_w, l)) in score {
            if l == 0 {
                a.push(id);
            } else if l == 1 {
                b.push(id);
            }
        }

        a.sort();
        b.sort();

        vec![a, b]
    }
}

fn main() {
    let tests = vec![
        (
            vec![
                vec![1, 3],
                vec![2, 3],
                vec![3, 6],
                vec![5, 6],
                vec![5, 7],
                vec![4, 5],
                vec![4, 8],
                vec![4, 9],
                vec![10, 4],
                vec![10, 9],
            ],
            vec![vec![1, 2, 10], vec![4, 5, 7, 8]],
        ),
        (
            vec![vec![2, 3], vec![1, 3], vec![5, 4], vec![6, 4]],
            vec![vec![1, 2, 5, 6], vec![]],
        ),
    ];

    for (matches, solution) in tests {
        let result = Solution::find_winners(matches);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
