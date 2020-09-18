struct CombinationIterator {
    chars: Vec<char>,
    combo_len: i32,
    _combos: Vec<Vec<char>>,
    _index: usize,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CombinationIterator {
    fn new(characters: String, combinationLength: i32) -> Self {
        let combos = Self::combos(
            &characters.chars().collect(),
            combinationLength as usize,
            0,
            vec![]
        );

        Self {
            chars: characters.chars().collect(),
            combo_len: combinationLength,
            _combos: combos,
            _index: 0,
        }
    }
    
    fn combos(n: &Vec<char>, r: usize, start: usize, pre: Vec<char>) -> Vec<Vec<char>> {
        if pre.len() == r {
            return vec![pre.clone()];
        }
        let mut out = Vec::new();
        for i in start..n.len() {
            let mut npre = pre.clone();
            npre.push(n[i].clone());
            out.extend(Self::combos(n, r, i + 1, npre));
        }

        out
    }

    fn next(&mut self) -> String {
        if !self.has_next() {
            panic!("End of combinations");
        }
        let s: String = self._combos[self._index].iter().collect();
        self._index += 1;

        s
    }

    fn has_next(&self) -> bool {
        self._index < self._combos.len()
    }
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * let obj = CombinationIterator::new(characters, combinationLength);
 * let ret_1: String = obj.next();
 * let ret_2: bool = obj.has_next();
 */

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_1() {
        let mut combo_iter = CombinationIterator::new("abcde".to_string(), 3);
        while combo_iter.has_next() {
            let s = combo_iter.next();
            println!("s = {:?}", s);
        }
    }

    #[test]
    fn test_2() {
        let chars: Vec<char> = "abcde".to_string().chars().collect();
        let combos = CombinationIterator::combos(&chars, 3, 0, vec![]);
        println!("combos = {:?}", combos);
    }
}
