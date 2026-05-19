// https://leetcode.com/problems/evaluate-reverse-polish-notation
struct Solution;

use std::collections::VecDeque;

#[derive(Debug)]
enum Operator {
    Add,
    Sub,
    Mul,
    Div,
}

impl Operator {
    fn parse(s: &str) -> Option<Operator> {
        match s {
            "+" => Some(Operator::Add),
            "-" => Some(Operator::Sub),
            "*" => Some(Operator::Mul),
            "/" => Some(Operator::Div),
            _ => None,
        }
    }

    fn exec(&self, a: i32, b: i32) -> i32 {
        match self {
            Operator::Add => a + b,
            Operator::Sub => a - b,
            Operator::Mul => a * b,
            Operator::Div => a / b,
        }
    }
}

#[derive(Debug)]
enum Token {
    Op(Operator),
    Num(i32),
}

impl Token {
    fn parse(s: &str) -> Token {
        match Operator::parse(s) {
            None => {
                let x: i32 = s.parse().expect("faild to parse string to i32");
                Token::Num(x)
            }
            Some(op) => Token::Op(op),
        }
    }
}

impl Solution {
    #[tracing::instrument(ret)]
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let n = tokens.len();
        let mut q: VecDeque<Token> = tokens.into_iter().map(|s| Token::parse(&s)).collect();
        let mut stack = Vec::with_capacity(n);

        while let Some(token) = q.pop_front() {
            tracing::info!(token=?token, stack=?stack, q=?q, "loop");
            match token {
                Token::Num(x) => {
                    stack.push(x);
                }
                Token::Op(op) => {
                    let b = stack.pop().expect("stack did not have 1 number(s) on top");
                    let a = stack.pop().expect("stack did not have 2 number(s) on top");
                    let c = op.exec(a, b);
                    stack.push(c);
                }
            }
        }

        let x = match stack.pop() {
            Some(x) => x,
            None => panic!("final stack was empty"),
        };
        assert!(stack.is_empty());

        x
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (vec!["2", "1", "+", "3", "*"], 9),
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
}
