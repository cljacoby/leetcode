use std::collections::HashMap;

struct Solution {}


// let mut map: HashMap<(usize, usize), f64> = HashMap::new();
// println!("i = {:?}, j = {:?}, max_mean = {:?}, mean = {:?}, slice = {:?}",
//     i, j, max_mean, mean, &nums[i..j]);


impl Solution {
    pub fn _find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        
        let mut i: usize = 0;
        let mut j = k as usize;
        let mut max_mean: f64 = std::f64::MIN;

        while j <= nums.len() {
            let mean = nums[i..j]
                .iter()
                .map(|i| *i as f64)
                .fold(0.0, |acc, x| acc + x) / k as f64;
            if mean > max_mean {
                max_mean = mean;
            }

            i += 1;
            j += 1
        }

        max_mean
    }

    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
       
        if k == 1 {
            return nums[0] as f64;
        }

        let mut i: usize = 0;
        let mut j = k as usize;
        let mut win_sum = nums[i..j].iter()
            .fold(0, |acc, x| acc + *x);
        let mut max_mean = win_sum as f64 / k as f64;

        loop {

            println!("i = {:?}, j = {:?}, win_sum = {:?}, max_mean = {:?}, slice = {:?}",
                i, j, win_sum, max_mean, &nums[i..j]);

            i += 1;
            j += 1;
            if j == nums.len() {
                break;
            }

            win_sum = win_sum - nums[i - 1] + nums[j];
            let new_mean = win_sum as f64 / k as f64;
            if new_mean > max_mean {
                max_mean = new_mean;
            }
        }

        max_mean
    }

}

mod tests {

    use super::*;

    #[test]
    fn test() {

        let v = vec![1, 12, -5, -6, 50, 3];
        let result = Solution::find_max_average(v, 4);
        assert_eq!(result, 12.75000);

        let v = vec![1, 3];
        let result = Solution::find_max_average(v, 2);
        assert_eq!(result, 2.0);

        let v = vec![1];
        let result = Solution::find_max_average(v, 1);
        assert_eq!(result, 1.0);
    }
}

fn main() {}
