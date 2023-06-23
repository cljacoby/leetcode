#include <stdio.h>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    struct ListNode *next;
};

void init_list_node(
    struct ListNode* node,
    int val,
    struct ListNode* next
) {
    node->val = val;
    node->next = next;
}

void print_list(struct ListNode* node) {
    if (node != NULL) {
        int first = 1;
        while (node != NULL) {
            if (!first) {
                printf("->");
            }
            printf("%d", node->val);
            first = 0;
            node = node->next;
        }
    }
    printf("\n");
}
