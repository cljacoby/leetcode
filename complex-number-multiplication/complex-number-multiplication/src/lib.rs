struct Solution;
type Sol=Solution;

impl Solution {

    // Leetcode is running an old version of the compiler where `std::string::String`
    // doesn't have `strip_prefix` method
    pub fn _deserialize(s: &String) -> (i32, i32) {
        let mut a = s
            .clone();
        let b = a
            .split_off(
                s.find('+')
                // Use of unwrap: Problem guarentees '+' delimiter
                .unwrap());
        let b = b.strip_prefix("+")
            // Use of unwrap: Problem guarentess '+' prefix 
            .unwrap();
            // Problem guarentees 'i' suffix
        let b = b.strip_suffix("i")
            .unwrap();

        // Use of unwrap: Problem format should guarentee parse result 
        (a.parse::<i32>().unwrap(), b.parse::<i32>().unwrap())
    }

    pub fn deserialize(s: &String) -> (i32, i32) {
        let v: Vec<&str> = s.trim_end_matches("i")
            .split('+')
            .collect();

        (v[0].parse::<i32>().unwrap(), v[1].parse::<i32>().unwrap())
    }
    
    
    pub fn serialize(num: &(i32, i32)) -> String {
        let (a, b) = num;
        format!("{}+{}i", a, b)
    }


    pub fn complex_number_multiply(a: String, b: String) -> String {
        let (a_real, a_i) = Sol::deserialize(&a);
        let (b_real, b_i) = Sol::deserialize(&b);

        let c_real = a_real * b_real - a_i * b_i; 
        let c_i = a_real * b_i + a_i * b_real;

        Sol::serialize(&(c_real, c_i))
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_deserialize() {
        let input = vec![
            "1+1i".to_string(),
            "0+0i".to_string(),
            "0+100i".to_string(),
            "100+-0i".to_string(),
        ];
        let output = vec![
            (1, 1),
            (0, 0),
            (0, 100),
            (100, 0),
        ];
        for (s, num) in input.into_iter().zip(output.into_iter()) {
            let result = Sol::deserialize(&s);
            assert_eq!(num, result);
        }
    }

    #[test]
    fn test_serialize() {
        let input = vec![
            (1, 1),
            (0, 0),
            (0, 100),
            (100, 0),
        ];
        let output = vec![
            "1+1i".to_string(),
            "0+0i".to_string(),
            "0+100i".to_string(),
            "100+0i".to_string(),
        ];
        for (num, s) in input.into_iter().zip(output.into_iter()) {
            let result = Sol::serialize(&num);
            assert_eq!(s, result);
        }
    
    }

    #[test]
    fn test_1() {
        let a = "1+1i".to_string();
        let b = "1+1i".to_string();
        let c = "0+2i".to_string();
        let result = Sol::complex_number_multiply(a, b);
        assert_eq!(c, result);
    }
    
    #[test]
    fn test_2() {
        let a = "1+-1i".to_string();
        let b = "1+-1i".to_string();
        let c = "0+-2i".to_string();
        let result = Sol::complex_number_multiply(a, b);
        assert_eq!(c, result);
    }
}

