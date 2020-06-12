#[derive(Debug)]
struct CustomStack {
    max_size: i32,
    stack: Vec<i32>
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CustomStack {

    fn new(maxSize: i32) -> Self {
        Self {
            max_size: maxSize,
            stack: Vec::with_capacity(maxSize as usize),
        }
    }
    
    fn push(&mut self, x: i32) {
        if self.max_size == self.stack.len() as i32 {
            return;
        }
        self.stack.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        match self.stack.pop() {
            Some(x) => x,
            None => -1,
        }
    }
    
    fn increment(&mut self, k: i32, val: i32) {
        let v: Vec<_> = self.stack.iter_mut()
            .enumerate()
            .filter(|(i, _)| i < &(k as usize))
            .map(|(_, x)| *x += val)
            .collect();
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * let obj = CustomStack::new(maxSize);
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * obj.increment(k, val);
 */

mod tests {

    use super::*;

    #[test]
    fn test() {
        let mut stack = CustomStack::new(5);
        stack.push(100);
        stack.push(200);
        stack.push(300);
        stack.push(400);
        stack.push(500);
        stack.increment(3, 10);
        assert_eq!(stack.pop(), 500);
        assert_eq!(stack.pop(), 400);
        assert_eq!(stack.pop(), 310);
        assert_eq!(stack.pop(), 210);
        assert_eq!(stack.pop(), 110);
    }
}
