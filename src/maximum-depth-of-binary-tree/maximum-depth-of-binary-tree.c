#include <stdio.h>
#include <assert.h>
#include "../tree_node.h"

int max(int a, int b) {
    if (a > b)
        return a;
    return b;
}

int maxDepth(struct TreeNode* root){
    if (root == NULL) {
        return 0;
    }
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

int main() {
    struct TreeNode n0, n1, n2, n3, n4;
    init_tree_node(&n0, 3, &n1, &n2);
    init_tree_node(&n1, 9, NULL, NULL);
    init_tree_node(&n2, 20, &n3, &n4);
    init_tree_node(&n3, 15, NULL, NULL);
    init_tree_node(&n4, 7, NULL, NULL);

    int solution = 3;
    int max_depth = maxDepth(&n0);
    printf("max_depth=%d solution=%d\n", max_depth, solution);
    assert(max_depth == solution);
    printf("success!\n");

    return 0;
}
