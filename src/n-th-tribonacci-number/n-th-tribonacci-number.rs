// https://leetcode.com/problems/n-th-tribonacci-number

#![allow(dead_code)]

struct Solution;
struct Solution1;

// Initial solution
impl Solution1 {

    pub fn tribonacci(n: i32) -> i32 {
        let n = n as usize;
        let mut v = Vec::with_capacity(n);
        v.extend_from_slice(&[0, 1, 1]);
        
        for i in 3..=n {
            let next = v[i - 3] + v[i - 2] + v[i - 1];
            v.push(next);
        }

        v[n]
    }
}

// Space optimiziation. Only keep three most recent entries.
impl Solution {

    pub fn tribonacci(n: i32) -> i32 {
        let n = n as usize;
        let mut v: [i32; 3] = [0, 1, 1];

        for i in 3..=n {
            let next = v[(i - 3) % 3]
                + v[(i - 2) % 3]
                + v[(i - 1) % 3];
            v[i % 3] = next;
        }

        v[n % 3]
    }
}

fn main() {
    let tests = vec![
        (4, 4),
        (25, 1389537),
    ];

    for (n, solution) in tests {
        let result = Solution::tribonacci(n);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
