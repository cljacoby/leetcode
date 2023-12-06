// https://leetcode.com/problems/count-of-matches-in-tournament

struct Solution;

impl Solution {
    pub fn number_of_matches(n: i32) -> i32 {
        let mut teams = n;
        let mut matches = 0;

        while teams > 1 {
            if teams % 2 == 0 {
                matches += teams / 2;
                teams /= 2;
            } else {
                matches += (teams - 1) / 2;
                teams = 1 + (teams - 1) / 2;
            }
        }

        matches
    }
}

fn main() {
    let tests = vec![
        (7, 6),
        (14, 13),
    ];
    for (teams, matches) in tests {
        let result = Solution::number_of_matches(teams);
        assert_eq!(result, matches);
    }
    println!("✅ All tests passed");
}
