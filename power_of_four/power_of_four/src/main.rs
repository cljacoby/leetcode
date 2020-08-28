struct Solution {
}

impl Solution {
    // Simple iterative solution
    pub fn _is_power_of_four(num: i32) -> bool {
        let mut i = 0;
        let mut product = 4_i32.checked_pow(i).unwrap();
        while product <= num {
            if product == num {
                return true;
            }
            i += 1;
            let opt = 4_i32.checked_pow(i);
            if opt.is_none() {
                return false;
            }
            product = opt.unwrap();
        }
        return false;
    }

    // Better solution; use logs 
    pub fn is_power_of_four(num: i32) -> bool {
        let power = (num as f64).log(4.0);
        power.fract() == 0.0
    }
}

fn main() {
    println!("{:?}", i32::MAX);
    println!("{:?}", 1162261466);
    let num = 5.0_f64.log(2.1_f64);
    println!("num = {:?}", num);
}

mod tests {

    use super::*;

    #[test]
    fn test() {
        assert!(Solution::is_power_of_four(4));
        assert!(Solution::is_power_of_four(16));
        assert!(!Solution::is_power_of_four(5));
        assert!(!Solution::is_power_of_four(100));
        assert!(Solution::is_power_of_four(64));
    }
}
