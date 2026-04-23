// https://leetcode.com/problems/min-stack
// struct Solution;

#[derive(Debug)]
struct MinStack {
    min: Option<i32>,
    stack: Vec<(i32, Option<i32>)>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    #[tracing::instrument(ret)]
    fn new() -> Self {
        let min: Option<i32> = None;
        let stack: Vec<(i32, Option<i32>)> = Vec::new();

        Self { min, stack }
    }
    
    #[tracing::instrument(ret)]
    fn push(&mut self, val: i32) {
        let node = (val, self.min);
        let new_min = match &self.min {
            None => val,
            Some(min) => i32::min(*min, val),
        };

        self.min = Some(new_min);
        self.stack.push(node);
    }
    
    #[tracing::instrument(ret)]
    fn pop(&mut self) {
        let (_val, new_min) = self.stack.pop()
            .expect("called pop on empty min_stack");
        self.min = new_min;
    }
    
    #[tracing::instrument(ret)]
    fn top(&self) -> i32 {
        let (val, _prev_min) = self.stack.last()
            .expect("called top on empty min_stack");

        val.to_owned()
    }
    
    #[tracing::instrument(ret)]
    fn get_min(&self) -> i32 {
        let min = self.min.clone()
            .expect("call get_min on empty min_stack");

        min
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let ops = vec![
        ("push".to_string(),    -2, None),
        ("push".to_string(),    0,  None),
        ("push".to_string(),    -3, None),
        ("getMin".to_string(),  -3, Some(-3)),
        ("pop".to_string(),  -3, None),
        ("top".to_string(),  -3, Some(0)),
        ("getMin".to_string(),  -3, Some(-2)),
    ];

    let mut min_stack = MinStack::new();
    for (method, arg, ret) in ops {
        match method.as_str() {
            "push" => {
                min_stack.push(arg);
            },
            "getMin" => {
                let out = min_stack.get_min();
                assert_eq!(Some(out), ret);
            },
            "pop" => {
                min_stack.pop();
            },
            "top" => {
                let out = min_stack.top();
                assert_eq!(Some(out), ret);

            },
            _ => panic!("invalid method in test config")
        }
    }


}
