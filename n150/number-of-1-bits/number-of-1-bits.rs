// https://leetcode.com/problems/number-of-1-bits

/** 
 * Notes:
 *  - SolutionA is the one I wrote first, and the one that's more intuitive to me,
 *    as someone who does not do bit-shifting and bit-mask type stuff on a regular basis
 *  - SolutionB is maybe the more "appropriate" codification if you're explicitly interested
 *    in operating on bits of data
 * */

struct SolutionA;
impl SolutionA {
    pub fn hamming_weight(mut n: i32) -> i32 {
        let mut count = 0;

        while n > 0 {
            if n % 2 != 0 {
                count += 1;
            }
            n /= 2;
        }

        count
    }
}

struct SolutionB;
impl SolutionB {
    pub fn hamming_weight(mut n: i32) -> i32 {
        let mut count = 0;

        while n > 0 {
            if n & 1 == 1 {
                count += 1;
            }
            n >>= 1;
        }

        count
    }
}

fn main() {
    let tests = vec![
        (11, 3),
        (128, 1),
        (2147483645, 30),
    ];

    for (n, solution) in tests {
        let res_a = SolutionA::hamming_weight(n);
        let res_b = SolutionB::hamming_weight(n);
        assert!(res_a == res_b && res_b == solution,
            "incorrect result, res_a={}, res_b={}, solution={}", res_a, res_b, solution);
    }

    println!("✅ All tests passed");


}
