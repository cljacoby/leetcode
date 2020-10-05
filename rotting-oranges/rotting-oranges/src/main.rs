use rotting_oranges::Solution;


fn main() {
    let grid = vec![
        vec![2,1,1],
        vec![1,1,0],
        vec![0,1,1]
    ];
    let solution = 4;
    assert_eq!(solution, Solution::oranges_rotting(grid));
}
