/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
*
 *
*You may assume the two numbers do not contain any leading zero, except the number 0 itself.
*
*Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
*Output: 7 -> 0 -> 8
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode previous = new ListNode(0);
    ListNode head = previous;
    int overflow = 0;

    while( l1 != null || l2 != null || overflow != 0){
        ListNode current = new ListNode(0);
        current.val = ((l1 == null) ? 0 : l1.val) + ((l2 == null) ? 0 : l2.val) + overflow;
        overflow = current.val/10;
        current.val=current.val%10;
        previous.next = current;
        previous = current;

        l1 = (l1 == null) ? l1 : l1.next;
        l2 = (l2 == null) ? l2 : l2.next;

    }
    return head.next;

}
}
/*
* Add values from both lists. If one list is null, add 0 instead. If both lists are null and there is no carryover, return.
* Mod the ListNode's elements by 10 and add the result to the next node.
* O(n) solution.
*/
