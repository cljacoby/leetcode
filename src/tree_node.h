#include <stdio.h>

/**
 * Definition for a binary tree node.
 */
typedef struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

void init_tree_node(
    TreeNode* node,
    int val,
    TreeNode* left,
    TreeNode* right
) {
    node->val = val;
    node->left = left;
    node->right = right;
}

void print_tree(
    TreeNode *node,
    unsigned int indent
) {
    if (node == NULL) {
        return;
    }
    for (unsigned int i = 0; i < indent; i++) {
        printf("  ");
    }
    printf("TreeNode { val: %d, L: %d, R: %d }\n",
        node->val,
        node->left == NULL ? 0 : 1,
        node->right == NULL ? 0 : 1
    );
    print_tree(node->left, indent + 1);
    print_tree(node->right, indent + 1);
}


/**
 * Caller must allocate `nodes` buffer with space for at least
 * `length` number of TreeNodes. The `length` should also be the same
 * length for the `values` array.
 *
 * Currently only supports trees where values are greater than 0,
 * as -1 is used to infer null values in the input array.
 * */
TreeNode* tree_from_array(
    TreeNode* nodes,
    const int* values,
    int length,
    int index
) {
    if (index >= length || values[index] == -1) {
        return NULL;
    }
    nodes[index].val = values[index];
    nodes[index].left = tree_from_array(nodes, values, length, 2 * index + 1);
    nodes[index].right = tree_from_array(nodes, values, length, 2 * index + 2);
    return &nodes[index];
}
