// https://leetcode.com/problems/evaluate-reverse-polish-notation
struct Solution;

enum Operation {
    Add,
    Subtract,
    Multiply,
    Divide,
}

impl Operation {
    pub fn get_operation(token: &str) -> Option<Self> {
        match token {
            "+" => Some(Self::Add),
            "-" => Some(Self::Subtract),
            "*" => Some(Self::Multiply),
            "/" => Some(Self::Divide),
            _ => None
        }
    }

    pub fn execute(a: i32, b: i32, op: &Operation) -> i32 {
        match op {
            Self::Add => a + b,
            Self::Subtract => a - b,
            Self::Multiply => a * b,
            Self::Divide => a / b,
        }
    }
}

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = vec![];
        for token in tokens {
            let top = match Operation::get_operation(&token) {
                Some(op) => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    Operation::execute(a, b, &op)
                },
                None => {
                    token.parse::<i32>().unwrap()
                }
            };
            stack.push(top);
        }

        stack.pop().unwrap()
    }
}

fn main() {
    let tests = vec![
        (vec!["2", "1", "+", "3", "*"], 9),
        (vec!["4", "13", "5", "/", "+"], 6),
        (vec!["18"], 18),
        (vec!["3","11","+","5","-"], 9),
        (
            vec![
                "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+",
            ],
            22,
        ),
    ];

    for (tokens, solution) in tests {
        let tokens = tokens.into_iter().map(|s| s.to_string()).collect();
        let result = Solution::eval_rpn(tokens);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
