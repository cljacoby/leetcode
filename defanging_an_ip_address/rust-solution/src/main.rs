struct Solution {}

impl Solution {
    // The signature is spelt wrong on leetest_caseode; change to this when submitting:
    //      pub fn defang_i_paddr(address: String) -> String
    pub fn defang_ip_addr(address: String) -> String {
        return address.replace(".", "[.]");
    }
}

fn main() {
    let input = "1.1.1.1";
    let output = "1[.]1[.]1[.]1";
    let result = Solution::defang_ip_addr(String::from(input));
    println!(
        "input = '{}'\noutput = '{}'\nresult = '{}'\n",
        input, output, result
    );
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test() {
        let test_cases = vec![
            ("", ""),
            (".", "[.]"),
            ("1.1.1.1", "1[.]1[.]1[.]1"),
            ("255.100.", "255[.]100[.]"),
            ("255_100_50_0", "255_100_50_0"),
        ];

        for (input, output) in test_cases.iter() {
            println!("input = {}, output = {}", input, output);
            let result = Solution::defang_ip_addr(String::from(*input));
            assert_eq!(result, String::from(*output));
        }
    }
}
