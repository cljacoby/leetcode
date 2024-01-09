#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "tree_node.h"

/** 
 * Assumptions:
 *  - Leetcode says max tree size will be 200 so we'll just allocate
 *    space for that many nodes up front
 *  - Assume input array does not contain negative values, which we'll
 *    use to represent NULL when building out the Tree.
 * */

const int TREE_MAX_SIZE = 200;

void leaf_array(TreeNode* node, int* leaf_arr, int* index, int length) {
    if (node == NULL) {
        return;
    }
    leaf_array(node->left, leaf_arr, index, length);
    if (node->left == NULL && node->right == NULL) {
        leaf_arr[*index] = node->val;
        (*index)++;
    }
    leaf_array(node->right, leaf_arr, index, length);
}

bool leafSimilar(TreeNode* root1, TreeNode* root2) {
    int arr1[TREE_MAX_SIZE];
    int arr2[TREE_MAX_SIZE];
    int idx1 = 0;
    int idx2 = 0;

    memset(arr1, 0, TREE_MAX_SIZE);
    memset(arr2, 0, TREE_MAX_SIZE);

    leaf_array(root1, arr1, &idx1, TREE_MAX_SIZE);
    leaf_array(root2, arr2, &idx2, TREE_MAX_SIZE);

    return memcmp(arr1, arr2, TREE_MAX_SIZE) == 0;
}

TreeNode* init_tree(int* v, int length) {
    TreeNode* tree = calloc(sizeof(TreeNode), TREE_MAX_SIZE);
    memset(tree, 0, TREE_MAX_SIZE);
    TreeNode* root = tree_from_array(tree, v, length, 0);
    print_tree(tree, 0);
    printf("\n");
    return root;
}

int main(void) {
    // int v1[] = {3,5,1,6,2,9,8,-1,-1,7,4};
    // int v2[] = {3,5,1,6,7,4,2,-1,-1,-1,-1,-1,-1,9,8};
    int v1[] = {4,2,6,1,3,5,7};
    int v2[] = {4,2,6,-1,3,5,7};
    TreeNode* t1 = init_tree(v1, sizeof(v1) / sizeof(int));
    TreeNode* t2 = init_tree(v2, sizeof(v2) / sizeof(int));
    
    char *s = leafSimilar(t1, t2) ? "true" : "false";
    printf("Leaf similar: %s\n", s);

    free(t1);
    free(t2);
}
