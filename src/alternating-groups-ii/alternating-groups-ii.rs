// https://leetcode.com/problems/alternating-groups-ii
struct Solution;

fn next(i: usize, len: usize) -> usize {
    (i + 1) % len
}

fn prev(i: usize, len: usize) -> usize {
    if i == 0 { len - 1 } else { i - 1 } 
}

fn size(i: usize, j: usize, len: usize) -> usize {
    if j >= i { j - i + 1 } else { len - i + j + 1 }
}

impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        let k = usize::try_from(k).expect("negative k");
        let len = colors.len();
        let mut count = 0;
        let mut start = 0;

        // Align `start` to a color group reset 
        for x in 0..len {
            let y = next(x, len);
            if colors[x] == colors[y] {
                start = y;
                break;
            }
        }

        let mut i = start;
        let mut j = next(i, len);
        let mut once = false;

        loop {
            if colors[j] == colors[prev(j, len)] {
                i = j;
                j = next(i, len);
                once = true;
            } else {
                if size(i, j, len) == k {
                    count += 1;
                    once = true;
                    i = next(i, len);
                }
                j = next(j, len);
            }

            if once && i == start {
                break
            }
        }

        count as i32
    }
}

struct S;

impl S {
    fn wrap(x: usize, len: usize) -> usize {
        x % len
    }

    fn prev(i: usize, len: usize) -> usize {
        let i = if i == 0 { len - 1 } else { i - 1 };
        S::wrap(i, len)
    }

    fn size(i: usize, j: usize, len: usize) -> usize {
        if j >= i { j - i + 1 } else { len - i + j + 1 }
    }

    pub fn number_of_alternating_groups(colors: Vec<i32>, k: i32) -> i32 {
        let k = usize::try_from(k).expect("negative k");
        let len = colors.len();
        let mut i = 0;
        let mut count = 0;


        for j in 1..(len + k - 1) {
            if colors[S::wrap(j, len)] == colors[S::prev(j, len)] {
                i = j;
            }
            if S::size(i, j, len) >= k {
                count += 1;
            }
        }

        count
    }
}

fn main() {
    let tests = vec![
        (vec![0,1,0,1,0], 3, 3),
        (vec![0,1,0,0,1,0,1], 6, 2),
        (vec![1,1,0,1], 4, 0),
        (vec![0,1,0,1], 3, 4),
    ];

    for (colors, k, solution) in tests.into_iter() {
        let r1 = Solution::number_of_alternating_groups(colors.clone(), k.clone());
        let r2 = S::number_of_alternating_groups(colors, k);
        assert_eq!(r1, solution);
        assert_eq!(r2, solution);
    }

    println!("✅ All tests passed")
}
