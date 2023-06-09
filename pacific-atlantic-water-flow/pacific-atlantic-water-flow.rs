// https://leetcode.com/problems/pacific-atlantic-water-flow

struct Solution;

use std::collections::HashSet;
use std::collections::HashMap;

impl Solution {
    pub fn pacific_atlantic(
        heights: Vec<Vec<i32>>
    ) -> Vec<Vec<i32>> {
        let rows = heights.len();
        let cols = heights[0].len();
        let mut out = Vec::with_capacity(rows);
        let mut seen = HashSet::with_capacity(rows * cols);
        let mut memo: HashMap<(usize, usize), usize> = HashMap::with_capacity(rows * cols);
        
        for (i, row) in heights.iter().enumerate() {
            for (j, _cell) in row.iter().enumerate() {
                let i = i as i32;
                let j = j as i32;
                let ret = Solution::step(
                    &heights,
                    &mut seen,
                    &mut memo,
                    i32::pow(10, 5) + 1,
                    i,
                    j,
                    rows,
                    cols
                );
                if ret == 3 {
                    out.push(vec![i as i32, j as i32]);
                }
            }
        }

        out
    }

    /*
     * Return is bit map representing which ocean this cell can reach.
     * Valid values:
     * - 0: Doesn't flow to any ocean
     * - 1: Flows to pacific (i.e. top and left borders)
     * - 2: Flows to atlantic (i.e. right and bottom borders)
     * - 3: Flows to both oceans
     * */
    fn step(
        heights: &Vec<Vec<i32>>,
        seen: &mut HashSet<(i32, i32)>,
        memo: &mut HashMap<(usize, usize), usize>,
        last: i32,
        i: i32,
        j: i32,
        rows: usize,
        cols: usize,
    ) -> usize {
        let coord = (i as usize, j as usize);
        if memo.contains_key(&coord) {
            return *memo.get(&coord).unwrap();
        }
        if i < 0 || j < 0 {
            return 1;
        }
        if i >= rows as i32 || j >= cols as i32 {
            return 2;
        }
        let curr = heights[i as usize][j as usize];
        if seen.contains(&(i, j)) || curr > last {
            return 0;
        }

        seen.insert((i,j));
        let res =
              Solution::step(heights, seen, memo, curr, i + 1, j, rows, cols)
            | Solution::step(heights, seen, memo, curr, i - 1, j, rows, cols)
            | Solution::step(heights, seen, memo, curr, i, j + 1, rows, cols)
            | Solution::step(heights, seen, memo, curr, i, j - 1, rows, cols);
        memo.insert(coord, res);
        seen.remove(&(i, j));

        res
    }
}

fn main() {
    let tests = vec![(
        vec![
            vec![1, 2, 2, 3, 5],
            vec![3, 2, 3, 4, 4],
            vec![2, 4, 5, 3, 1],
            vec![6, 7, 1, 4, 5],
            vec![5, 1, 1, 2, 4],
        ],
        vec![
            vec![0, 4],
            vec![1, 3],
            vec![1, 4],
            vec![2, 2],
            vec![3, 0],
            vec![3, 1],
            vec![4, 0],
        ],
    )];

    for (heights, solution) in tests {
        let result = Solution::pacific_atlantic(heights);
        assert_eq!(result, solution);
        println!("✅ All tests passed")
    }
}
