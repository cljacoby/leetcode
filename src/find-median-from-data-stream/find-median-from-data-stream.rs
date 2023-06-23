// https://leetcode.com/problems/find-median-from-data-stream

#[derive(Debug)]
struct MedianFinder {
    nums: Vec<i32>,
}

/*
 * Kinda cheated here. I think the intention was that instead of using a provided `binary_search`
 * method, you would write that part yourself.
 * */

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
        MedianFinder { nums: Vec::with_capacity(5000) }
    }

    fn binary_search(
        nums: &Vec<i32>,
        target: i32,
        i: usize,
        j: usize
    ) -> Result<usize, usize> {
        let len = j - i;
        let mid =  i + (len / 2);
        // println!("start bin search. tg={:?}, i={:?}, j={:?}, len={:?}, mid={:?}, nums={:?}",
        //     target, i, j, len, mid, &nums[i..j]);
        if len == 0 {
            return Err(i);
        }
        if len == 1  {
            if nums[i] == target {
                return Ok(i);
            } else {
                return Err(i + 1);
            }
        }
        if target < nums[mid] {
            MedianFinder::binary_search(nums, target, i, mid)
        } else {
            MedianFinder::binary_search(nums, target, mid, j)
        }
    }
    
    fn add_num(&mut self, num: i32) {
        
        // Easy mode is using the Vec built-in method.
        // match self.nums.binary_search(&num) {}
        

        match MedianFinder::binary_search(&self.nums, num, 0, self.nums.len()) {
            Ok(idx) => self.nums.insert(idx, num),
            Err(idx) => self.nums.insert(idx, num),
        }
    }
    
    fn find_median(&self) -> f64 {
        let mid = self.nums.len() / 2;
        println!("mid = {:?}", mid);
        if self.nums.len() % 2 == 0 {
            (self.nums[mid - 1] as f64 + self.nums[mid] as f64) / 2.0
        } else {
            self.nums[mid] as f64
        }
    }

}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

fn main() {
    // let v = vec![0, 1, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
    // let res = MedianFinder::binary_search(&v, 13, 0, v.len());
    // println!("res = {:?}", res);
    // let res = MedianFinder::binary_search(&v, 4, 0, v.len());
    // println!("res = {:?}", res);
    // let res = MedianFinder::binary_search(&v, 100, 0, v.len());
    // println!("res = {:?}", res);

    let mut med_find = MedianFinder::new();
    med_find.add_num(1);
    med_find.add_num(4);
    println!("med_find = {:?}", med_find);
    let m = med_find.find_median();
    println!("m = {:?}", m);
    
    med_find.add_num(3);
    println!("med_find = {:?}", med_find);
    let m = med_find.find_median();
    println!("m = {:?}", m);

}
