
#[derive(Debug)]
pub struct BSTNode<T: PartialOrd> {
    pub value: T,
    pub left: Option<Box<BSTNode<T>>>,
    pub right: Option<Box<BSTNode<T>>>,
}

impl<T: PartialOrd> BSTNode<T> {
    fn new(value: T) -> Self {
        Self {
            value,
            left: None,
            right: None,
        }
    }

    fn insert(&mut self, value: T) {
        if value < self.value {
            match self.left {
                Some(ref mut node) => { node.insert(value); },
                None => { self.left = Some(Box::new(BSTNode::new(value))) },
            }
        } else {
            match self.right {
                Some(ref mut node) => { node.insert(value); },
                None => { self.right = Some(Box::new(BSTNode::new(value))) },
            }
        }
    }

    fn has(&self, value: T) -> bool {
        if value == self.value {
            return true;
        }
        if value < self.value {
            match self.left {
                Some(ref node) => { node.has(value) },
                None => { false }
            }
        } else {
            match self.right {
                Some(ref node) => { node.has(value) },
                None => { false }
            }
        }
    }

    fn traverse(node: &Option<Box<BSTNode<T>>>)
        where T: std::fmt::Debug
    {
        match node {
            None => {
                return;
            },
            Some(ref node) => {
                BSTNode::traverse(&node.left);
                println!("{:?}", node.value);
                BSTNode::traverse(&node.right);
            }
        }
    }

}

#[derive(Debug)]
pub struct BST<T: PartialOrd> {
    root: Option<BSTNode<T>>,
}

impl<T: PartialOrd> BST<T> {
    pub fn new() -> Self {
        Self { root: None }
    }

    pub fn insert(&mut self, value: T) {
        match self.root {
            None => { self.root = Some(BSTNode::new(value)); },
            Some(ref mut node) => { node.insert(value); }
        }
    }

    pub fn has(&self, value: T) -> bool {
        match self.root {
            None => { false },
            Some(ref node) => { node.has(value) }
        }
    }
}

mod tests {

    use super::*;

    fn create_test_tree(root: i32, v: Vec<i32>) -> BSTNode<i32> {
        let mut node = BSTNode::new(root);
        for i in v {
            node.insert(i);
        }

        node
    }

    #[test]
    fn test_node_insert() {
        let root = create_test_tree(5, vec![1, 0, 3, 7, 8, 9]);
        println!("root = {:#?}", root);
    }

    #[test]
    fn test_node_has() {
        let v = vec![1, 0, 3, 7, 9];
        let root = create_test_tree(5, v.clone());
        
        assert!(root.has(5));
        for i in v {
            assert!(root.has(i));
        }
    }

    #[test]
    fn test_node_traverse() {
        let root = create_test_tree(5, vec![1, 0, 3, 7, 8, 9]);
        BSTNode::traverse(&Some(Box::new(root)));
    }

}