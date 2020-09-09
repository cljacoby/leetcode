struct Solution;

// -----

type Sol = Solution;
use std::cmp::Ordering;

impl Solution {
    pub fn sum_row(row: &Vec<i32>) -> i32 {
        let mut sum = 0;
        for i in row.iter() {
            if *i == 0 {
                return sum;
            };
            sum += *i;
        }

        sum
    }

    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut map: Vec<(i32, i32)> = Vec::with_capacity(k as usize);

        for (i, row) in mat.iter().enumerate() {
            let sum = Sol::sum_row(row);
            map.push((i as i32, sum));
        }

        map.sort_by(|(row_1, count_1), (row_2, count_2)| {
            match count_1.partial_cmp(count_2).unwrap() {
                Ordering::Less => Ordering::Less,
                Ordering::Greater => Ordering::Greater,
                Ordering::Equal => {
                    if row_1 < row_2 {
                        Ordering::Less
                    } else {
                        Ordering::Greater
                    }
                }
            }
        });

        map[0..k as usize].iter().map(|(row, count)| *row).collect()
    }
}

fn main() {
    let result = Sol::k_weakest_rows(
        vec![
            vec![1, 1, 0, 0, 0],
            vec![1, 1, 1, 1, 0],
            vec![1, 0, 0, 0, 0],
            vec![1, 1, 0, 0, 0],
            vec![1, 1, 1, 1, 1],
        ],
        3,
    );
    println!("result = {:?}", result);
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_1() {
        let result = Sol::k_weakest_rows(
            vec![
                vec![1, 1, 0, 0, 0],
                vec![1, 1, 1, 1, 0],
                vec![1, 0, 0, 0, 0],
                vec![1, 1, 0, 0, 0],
                vec![1, 1, 1, 1, 1],
            ],
            3,
        );
        assert_eq!(result, vec![2, 0, 3]);
    }

    #[test]
    fn test_2() {
        let result = Sol::k_weakest_rows(
            vec![
                vec![1, 0, 0, 0],
                vec![1, 1, 1, 1],
                vec![1, 0, 0, 0],
                vec![1, 0, 0, 0],
            ],
            2,
        );
        assert_eq!(result, vec![0, 2]);
    }
}
