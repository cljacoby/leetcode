struct Solution;
type Sol=Solution;

impl Solution {

    pub fn is_subsequence(mut s: String, mut t: String) -> bool {
        'outer: while let Some(c1) = s.pop() {
            if t.len() == 0 {
                return false;
            }
            'inner: while let Some(c2) = t.pop() {    
                if c1 == c2 {
                    continue 'outer;
                }
                if t.len() == 0 && s.len() == 0 {
                    return false;
                }
            }
        }

        s.len() == 0
    }
}


#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_1() {
        let s = "abc".to_string();
        let t = "ahbgdc".to_string();
        let result = Sol::is_subsequence(s, t);
        assert_eq!(result, true);
    }

    #[test]
    fn test_2() {
        let s = "axc".to_string();
        let t = "ahbgdc".to_string();
        let result = Sol::is_subsequence(s, t);
        assert_eq!(result, false);
    }
   
    #[test]
    fn test_3() {
        let s = "aaaaaa".to_string();
        let t = "bbaaaa".to_string();
        let result = Sol::is_subsequence(s, t);
        assert_eq!(result, false);
    }
    
    #[test]
    fn test_4() {
        let s = "b".to_string();
        let t = "c".to_string();
        let result = Sol::is_subsequence(s, t);
        assert_eq!(result, false);
    }

}
