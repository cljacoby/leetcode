struct Solution;
type Sol=Solution;

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let len = gas.len();
        'outer: for start in 0..len {
            let mut sum = 0;
            for i in 0..len {
                // Iteration begins at index equal to `start`, and wraps around
                let i = (i + start) % len;
                sum += gas[i];
                sum -= cost[i];
                if sum < 0 {
                    continue 'outer;
                }
            }
            return start as i32;
        }
        
        -1
    }
}

#[cfg(test)]
mod tests {
    
    use super::*;

    #[test]
    fn test_1() {
        let result = Sol::can_complete_circuit(
            vec![1,2,3,4,5],    // gas
            vec![3,4,5,1,2],    // cost
        );
        assert_eq!(result, 3);
    }
    
    #[test]
    fn test_2() {
        let result = Sol::can_complete_circuit(
            vec![2,3,4],    // gas
            vec![3,4,3],    // cost
        );
        assert_eq!(result, -1);
    }
}

fn main() {}
