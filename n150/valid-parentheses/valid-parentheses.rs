// https://leetcode.com/problems/valid-parentheses
struct Solution;

use std::collections::VecDeque;

#[derive(Debug)]
enum Position {
    Open(Brace),
    Close(Brace),
}

#[derive(Debug, PartialEq)]
enum Brace {
    Parenthesis,
    Square,
    Angle,
}

impl From<char> for Position {
    fn from(ch: char) -> Self {
        match ch {
            '(' => Self::Open(Brace::Parenthesis),
            ')' => Self::Close(Brace::Parenthesis),
            '[' => Self::Open(Brace::Square),
            ']' => Self::Close(Brace::Square),
            '{' => Self::Open(Brace::Angle),
            '}' => Self::Close(Brace::Angle),
            _ => panic!("invalid bracket character"),
        }
    }
}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut braces: VecDeque<Position> = s.chars()
            .into_iter()
            .map(|ch| Position::from(ch))
            .collect();

        let mut stack: Vec<Brace> = Vec::with_capacity(braces.len());

        while let Some(pos) = braces.pop_front() {
            match pos {
                Position::Open(b) => {
                    stack.push(b);
                },
                Position::Close(close) => {
                    let open = match stack.pop() {
                        None => return false,
                        Some(open) => open,
                    };
                    if open != close {
                        return false
                    }
                },
            }
        }

        stack.is_empty()
    }
}

fn main() {
    let tests = vec![
        (
            "()[]{}".to_string(),
            true,
        ),
        (
            "(]".to_string(),
            false,
        ),
        (
            "([])".to_string(),
            true,
        ),
        (
            "([)]".to_string(),
            false,
        ),
    ];

    for (s, solution) in tests {
        let result = Solution::is_valid(s);
        assert_eq!(result, solution);
    }

}
