// https://leetcode.com/problems/k-closest-points-to-origin
struct Solution;

impl Solution {

    #[tracing::instrument(ret)]
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut kpoints: Vec<(f64, Vec<i32>)> = points
            .into_iter()
            .map(|point| {
                let a = point.get(0).expect("point had no elements, expected 2");
                let b = point.get(1).expect("point had 1 elements, expected 2");
                let prod = i32::pow(*a, 2) + i32::pow(*b, 2);
                let mag = (prod as f64).sqrt();

                (mag, point)
            })
        .collect();
        
        kpoints.sort_by(|a, b| a.0.total_cmp(&b.0));
        tracing::info!(kpoints=?kpoints, "sorted");
        debug_assert!(kpoints.len() >= (k as usize));

        let out = kpoints
            .into_iter()
            .take(k as usize)
            .map(|(_mag, point)| point).collect();

        out
    }
}

fn main() {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .init();

    let tests = vec![
        (
            vec![vec![1,3],vec![-2,2]],
            1,
            vec![vec![-2,2]]
        ),
    ];

    for (points, k, solution) in tests {
        let result = Solution::k_closest(points, k);
        assert_eq!(result, solution);
    }

}
