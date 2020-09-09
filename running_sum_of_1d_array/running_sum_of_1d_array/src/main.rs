struct Solution;
type Sol = Solution;

impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut sum = 0;
        nums.iter()
            .map(|i| {
                sum += i;
                sum
            })
            .collect()
    }
}

fn main() {}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![1, 2, 3, 4];
        let rsum = Sol::running_sum(nums);
        println!("rsum = {:?}", rsum);
        assert_eq!(rsum, vec![1, 3, 6, 10]);
    }

    fn test_2() {
        let nums = vec![1, 1, 1, 1, 1];
        let rsum = Sol::running_sum(nums);
        println!("rsum = {:?}", rsum);
        assert_eq!(rsum, vec![1, 2, 3, 4, 5]);
    }
}
