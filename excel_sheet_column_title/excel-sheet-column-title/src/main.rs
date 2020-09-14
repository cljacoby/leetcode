use std::collections::HashMap;

struct Solution;
type Sol = Solution;

impl Solution {
    pub fn char_map() -> HashMap<i32, char> {
        vec![
            (1, 'A'),
            (2, 'B'),
            (3, 'C'),
            (4, 'D'),
            (5, 'E'),
            (6, 'F'),
            (7, 'G'),
            (8, 'H'),
            (9, 'I'),
            (10, 'J'),
            (11, 'K'),
            (12, 'L'),
            (13, 'M'),
            (14, 'N'),
            (15, 'O'),
            (16, 'P'),
            (17, 'Q'),
            (18, 'R'),
            (19, 'S'),
            (20, 'T'),
            (21, 'U'),
            (22, 'V'),
            (23, 'W'),
            (24, 'X'),
            (25, 'Y'),
            (0, 'Z'),
        ]
            .into_iter()
            .collect()
    }
    
    pub fn convert_to_title(mut n: i32) -> String {
        let map = Sol::char_map();
        let mut chars: Vec<char> = Vec::new();
        let one_more = true;
        
        while n > 0 {
            let modu = n % 26;
            // Edge case: If n=26, we wind up doing an extra iteration and adding an 'A'. 
            if n == 26 {
                n = (n - modu) / 26 - 1;
            } else {
                n = (n - modu) / 26;
            }
            let c = map.get(&modu).unwrap();
            chars.push(*c);
        } 


        chars
            .into_iter()
            .rev()
            .collect()
    }
}

fn main() {}


#[cfg(test)]
mod tests {
    
    use super::*;

    #[test]
    fn test_1() {
        let s = Sol::convert_to_title(701);
        println!("s = {:?}", s);
        assert_eq!(s, "ZY".to_string())
    }

    #[test]
    fn test_2() {
        let s = Sol::convert_to_title(1);
        println!("s = {:?}", s);
        assert_eq!(s, "A".to_string())
    }

    #[test]
    fn test_3() {
        let s = Sol::convert_to_title(28);
        println!("s = {:?}", s);
        assert_eq!(s, "AB".to_string())
    }

    #[test]
    fn test_4() {
        let s = Sol::convert_to_title(26);
        println!("s = {:?}", s);
        assert_eq!(s, "Z".to_string())
    }
    #[test]
    fn test_5() {
        let s = Sol::convert_to_title(676);
        println!("s = {:?}", s);
        assert_eq!(s, "ZZ".to_string())
    }
    #[test]
    fn test_6() {
        let s = Sol::convert_to_title(52);
        println!("s = {:?}", s);
        assert_eq!(s, "ZZ".to_string())
    }

}
