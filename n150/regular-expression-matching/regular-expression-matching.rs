use tracing::{info, error};
use tracing_tree::HierarchicalLayer;
use tracing_subscriber::EnvFilter;
use tracing_subscriber::{Registry, prelude::*};

// https://leetcode.com/problems/regular-expression-matching
struct Solution;

use std::collections::VecDeque;

#[derive(Debug, Clone)]
enum Pattern {
    Dot,
    Char(char),
}

#[derive(Debug, Clone)]
enum Op {
    Single(Pattern),
    Multi(Pattern),
}

impl From<char> for Pattern {
    fn from(ch: char) -> Self {
        match ch {
            '.' => Self::Dot,
            _ => Self::Char(ch),
        }
    }
}

impl Solution {
    #[tracing::instrument(ret)]
    pub fn is_match(s: String, p: String) -> bool {
        Self::try_is_match(s, p).unwrap_or(false)
    }
    
    #[tracing::instrument(ret)]
    pub fn try_is_match(s: String, p: String) -> Option<bool> {
        assert!(s.is_ascii(), "input string not ascii");
        assert!(p.is_ascii(), "input pattern not ascii");

        // queue of input characters
        let mut s = VecDeque::from(s.chars().collect::<Vec<char>>());

        // queue of operations
        let mut p: VecDeque<char> = p.chars().collect();
        let mut ops: VecDeque<Op> = VecDeque::with_capacity(p.len());
        while let Some(pat) = p.pop_front() {
            if pat == '*' {
                panic!("invalid asterix operator");
            }

            let pat = Pattern::from(pat);
            let op = if p.front() == Some(&'*') {
                p.pop_front().unwrap();
                Op::Multi(pat)
            } else {
                Op::Single(pat)
            };

            ops.push_back(op);
        } 

        info!(ops=?ops, s=?s, "initial state");

        while let Some(op) = ops.pop_front() {
            // if s.is_empty() {
            //     break
            // }

            match op {
                Op::Single(pat) => {
                    Self::apply_exact_once(pat, &mut s)?;
                }
                Op::Multi(pat) => {
                    Self::apply_once_or_more(pat, &mut s);
                },
            }
        }

        Some(s.is_empty())
    }
    
    #[tracing::instrument(ret)]
    pub fn apply_once_or_more(pat: Pattern, s: &mut VecDeque<char>) {
        while let Some(ch) = s.pop_front() {
            if let Pattern::Char(expected) = pat {
                if ch != expected {
                    info!(ch=?ch, expected=?expected, "did not match expected char");
                    s.push_front(ch);
                    break;
                }
            }
        }
    }

    #[tracing::instrument(ret)]
    pub fn apply_exact_once(pat: Pattern, s: &mut VecDeque<char>) -> Option<()> {
        let ch = s.pop_front().or_else(|| {
            info!(pat=?pat, s=?s, "input exhausted");
            None
        })?;

        if let Pattern::Char(expected) = pat {
            if ch != expected {
                info!(pat=?pat, expected=?expected, "did not match expected char");
                return None;
            }
        }

        Some(())
    }
}

fn main() {
    Registry::default()
        .with(EnvFilter::from_default_env())
        .with(HierarchicalLayer::new(2).with_targets(true))
        .init();

    let tests = vec![
        (
            "aa".to_string(),
            "aa".to_string(),
            true,
        ),
        (
            "aa".to_string(),
            "a".to_string(),
            false,
        ),
        (
            "aa".to_string(),
            "a*".to_string(),
            true,
        ),
        (
            "aa".to_string(),
            "a.".to_string(),
            true,
        ),
        (
            "aa".to_string(),
            ".*".to_string(),
            true,
        ),
        (
            "aab".to_string(),
            "a*b".to_string(),
            true,
        ),
        (
            "aaa".to_string(),
            "a*b".to_string(),
            false,
        ),
        (
            "aab".to_string(),
            "c*a*b".to_string(),
            true,
        ),
    ];

    for (s, p, solution) in tests {
        let result = Solution::is_match(s.clone(), p.clone());
        assert_eq!(result, solution, "s={:?}, p={:?}", s, p);
    }

}
