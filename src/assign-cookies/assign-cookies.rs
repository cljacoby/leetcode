// https://leetcode.com/problems/assign-cookies
struct Solution;


impl Solution {
    fn rev(a: &i32, b: &i32) -> std::cmp::Ordering {
        b.partial_cmp(&a).unwrap()
    }

    pub fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
        if g.len() == 0 || s.len() == 0 {
            return 0;
        }
        g.sort_by(Self::rev);
        s.sort_by(Self::rev);
        let mut count = 0;

        while let Some(cookie) = s.pop() {
            match g.last() {
                None => break,
                Some(child) => {
                    if cookie >= *child {
                        g.pop();
                        count += 1;
                    }
                },
            };
        }

        count
    }
}

fn main() {
    let tests = vec![
        (vec![1, 2, 3], vec![1, 1], 1),
        (vec![1, 2], vec![1, 2, 3], 2),
        (vec![10,9,8,7], vec![5,6,7,8], 2),
    ];

    for (g, s, solution) in tests {
        let result = Solution::find_content_children(g, s);
        assert_eq!(result, solution);
    }

    println!("✅ All tests passed")
}
