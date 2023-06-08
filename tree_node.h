/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void init_tree_node(
    struct TreeNode* node,
    int val,
    struct TreeNode* left,
    struct TreeNode* right
) {
    node->val = val;
    node->left = left;
    node->right = right;
}
