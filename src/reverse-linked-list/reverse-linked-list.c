#include <stdio.h>
#include <assert.h>
#include "../list_node.h"

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL) {
        return NULL;
    }

    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    struct ListNode* tmp = NULL;
    
    while (curr != NULL) {
        tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }

    return prev;
}

int main() {
    struct ListNode n1, n2, n3, n4, n5, rev;
    
    init_list_node(&n1, 1, &n2);
    init_list_node(&n2, 2, &n3);
    init_list_node(&n3, 3, &n4);
    init_list_node(&n4, 3, &n5);
    init_list_node(&n5, 5, NULL);

    print_list(&n1);
    rev = *reverseList(&n1);
    print_list(&rev);

    return 0;
}
