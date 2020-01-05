struct Solution{}

impl Solution {

    // The signature is spelt wrong on leetcode; change to this when submitting:
    // pub fn defang_i_paddr(address: String) -> String
    pub fn defang_ip_addr(address: String) -> String {
        return address.replace(".", "[.]");
    }

}

fn main() {
    println!("main");
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test() {}

}
