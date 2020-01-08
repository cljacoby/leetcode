// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

struct Solution;

impl Solution {
    pub fn ll_to_vec(head: ListNode) -> Vec<i32> {
        let mut v = vec![head.val];
        let mut node = &head;
        while let Some(next) = &node.next {
            v.push(next.val);
            node = next;
        }

        v
    }

    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        if let Some(_) = head {} else { return -1; };

        
        let v = Solution::ll_to_vec(*(head.unwrap()));
        let mut total = 0;
        let mut place = 0;
        for val in v.iter().rev() {
            let add = i32::pow(2, place) * val;
            place += 1;
            total += add;
        }

        total
    }
}

fn main() {
    
    // eww
    let head = Box::new(ListNode {
        val: 1,
        next: Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode { val: 1, next: None })),
        })),
    });

    let result = Solution::get_decimal_value(Some(head));
    // println!("get_decimal_value({:?}) = {:?}",
    //     Solution::ll_to_vec(head.unwrap()),
    //     result);
    println!("result = {:?}", result);
}
