#include <stdio.h>
#include <assert.h>
#include "../tree_node.h"

struct TreeNode* invertTree(struct TreeNode* root){
    if (root == NULL) {
        return NULL;
    }
    
    invertTree(root->left);
    invertTree(root->right);

    struct TreeNode* tmp = NULL;
    tmp = root->left;
    root->left = root->right;
    root->right = tmp;

    return root;
}

int main() {
    struct TreeNode n0, n1, n2, n3, n4, n5, n6;
    
    init_tree_node(&n1, 2, &n3, &n4);
    init_tree_node(&n3, 1, NULL, NULL);
    init_tree_node(&n4, 3, NULL, NULL);
    
    init_tree_node(&n2, 7, &n5, &n6);
    init_tree_node(&n5, 6, NULL, NULL);
    init_tree_node(&n6, 9, NULL, NULL);

    init_tree_node(&n0, 4, &n1, &n2);

    print_tree(&n0, 0);
    invertTree(&n0);
    print_tree(&n0, 0);

    return 0;
}
