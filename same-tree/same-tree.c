#include "../tree_node.h"
#include "stdbool.h"
#include "assert.h"

bool isSameTree(struct TreeNode* a, struct TreeNode* b) {
    if (a == NULL && b == NULL) {
        return true;
    }

    if ((a == NULL && b != NULL)
        || (b == NULL && a != NULL)
        || (a->val != b->val)
    ) {
        return false;
    }

    return isSameTree(a->left, b->left)
        && isSameTree(a->right, b->right);
}


int main(void) {
    struct TreeNode a0, a1, a2;
    init_tree_node(&a0, 0, &a1, &a2);
    init_tree_node(&a1, 1, NULL, NULL);
    init_tree_node(&a2, 2, NULL, NULL);
    
    struct TreeNode b0, b1, b2;
    init_tree_node(&b0, 0, &b1, &b2);
    init_tree_node(&b1, 1, NULL, NULL);
    init_tree_node(&b2, 2, NULL, NULL);

    bool res = isSameTree(&a0, &b0);
    printf("res = %d\n", res);
    assert(res);

    return 0;
}
