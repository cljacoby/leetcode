struct Solution;

/*
 * Note:
 *
 * My first attempt at the solution isn't totally a wash;
 * however, I can't simply translate the input to a u32, u64, u128, etc. as
 * there are test cases that exceed all of these.
 *
 * Intead, it seems like I need to use some intermediary data structure
 * where you basically have an array of magnitudes to multiply against a
 * factor of 10.
 * */

impl Solution {

    pub fn int_to_char(i: u128) -> char {
        match i {
            0 => '0',
            1 => '1',
            2 => '2',
            3 => '3',
            4 => '4',
            5 => '5',
            6 => '6',
            7 => '7',
            8 => '8',
            9 => '9',
            _ => { panic!("Only accepts integer values [0,1,2,3,4,5,6,7,8,9]") }
        }
    }

    pub fn char_to_int(c: char) -> u128 {
        match c {
            '0' => 0,
            '1' => 1,
            '2' => 2,
            '3' => 3,
            '4' => 4,
            '5' => 5,
            '6' => 6,
            '7' => 7,
            '8' => 8,
            '9' => 9,
            _ => { panic!("Only accepts character values [0,1,2,3,4,5,6,7,8,9]") }
        }
    }

    pub fn string_to_int(s: String) -> u128 {
        let mut product = 0;
        for (i, c) in s.chars().rev().enumerate() {
            product += Solution::char_to_int(c) * 10u128.pow(i as u32);
        }

        product
    }

    pub fn int_to_string(mut num: u128) -> String {
        let mut digits: Vec<char> = vec![];


        // put overflow check

        loop {
            let digit = Solution::int_to_char(num % 10);
            digits.push(digit);
            num = num / 10;
            if num == 0 {
                break;
            }
        }

        digits.iter().rev().collect()
    }

    pub fn multiply(num1: String, num2: String) -> String {
        Solution::int_to_string(
            Solution::string_to_int(num1) * Solution::string_to_int(num2)
        )
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_string_to_int() {

        let pairs: Vec<(String, u128)> = vec![
            ("114".to_string(), 114),
            ("0".to_string(), 0),
            ("1".to_string(), 1),
            ("1123323".to_string(), 1123323),
            (u64::MIN.to_string(), 0),
            // u32::MAX => 4294967295
            (u32::MAX.to_string(), 4294967295),
            // u64::MAX => 18446744073709551615
            (u64::MAX.to_string(), 18446744073709551615),

            ("498828660196".to_string(), 498828660196),
            ("840477629533".to_string(), 840477629533),
        ];

        for (s, answer) in pairs {
            let result = Solution::string_to_int(s);
            assert_eq!(result, answer);
        }
    }

    #[test]
    fn test_int_to_string() {
        let pairs: Vec<(u128, String)> = vec![
            (114, "114".to_string()),
            (0, "0".to_string()),
            (1, "1".to_string()),
            (u32::MAX as u128, "4294967295".to_string()),
            (u64::MAX as u128, "18446744073709551615".to_string()),

            (498828660196, "498828660196".to_string()),
            (840477629533, "840477629533".to_string()),
        ];

        for (num, answer) in pairs {
            let result = Solution::int_to_string(num);
            assert_eq!(result, answer);
        }
    }


    #[test]
    fn test_multiply() {
        let trios = vec![
            ("10".to_string(), "10".to_string(), "100".to_string()),
            ("12".to_string(), "12".to_string(), "144".to_string()),
            ("1".to_string(), "1".to_string(), "1".to_string()),
            ("1".to_string(), "0".to_string(), "0".to_string()),
            ("498828660196".to_string(), "840477629533".to_string(), "419254329864656431168468".to_string()),
        ];

        for (fact1, fact2, answer) in trios {
            let fact1 = Solution::string_to_int(fact1);
            let fact2 = Solution::string_to_int(fact2);
            let result = Solution::int_to_string(fact1 * fact2);
            assert_eq!(result, answer);
        }
    }


}
