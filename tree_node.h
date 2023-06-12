#include <stdio.h>

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

void print_tree(
    struct TreeNode *node,
    unsigned int indent
) {
    if (node == NULL) {
        return;
    }
    for (unsigned int i = 0; i < indent; i++) {
        printf("  ");
    }
    printf("TreeNode { val: %d }\n", node->val);
    print_tree(node->left, indent + 1);
    print_tree(node->right, indent + 1);
}
