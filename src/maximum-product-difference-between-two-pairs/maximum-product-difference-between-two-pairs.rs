// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

/** 
 * Snag I was hitting was recognizing that you temporarily
 * set a single (idx,val) as both a max and a min, and rely on there
 * being a guaranteed solution (a!=b!=c!=d) to eventually resolve this.
 *
 * I was struggling with the idea that if we move out an old max,
 * don't we need to re-assess if it might be a new min? I think it's
 * possible to code it this way, it was just getting messy.
 * */

struct Solution;

impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let mut mn = (i32::MAX, i32::MAX);
        let mut mx = (i32::MIN, i32::MIN);

        for num in nums {
            if num > mx.1 {
                mx.0 = mx.1;
                mx.1 = num;
            } else if num > mx.0 {
                mx.0 = num;
            }

            if num < mn.1 {
                mn.0 = mn.1;
                mn.1 = num;
            } else if num < mn.0 {
                mn.0 = num;
            }
        }

        (mx.1 * mx.0) - (mn.1 * mn.0)
    }
}

fn main() {
    let tests = vec![
        (vec![5,6,2,7,4], 34),
        (vec![4,2,5,9,7,4,8], 64),
    ];

    for (arr, solution) in tests {
        let result = Solution::max_product_difference(arr);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
