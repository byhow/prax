package com.acme;

public class SwapNodesInPairs {

//      Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode swapPairs(ListNode head) {
        ListNode tmp = new ListNode(0);
        tmp.next = head;
        ListNode cur = tmp;

        while (cur.next != null && cur.next.next != null) {
            ListNode first = cur.next;
            ListNode sec = cur.next.next;
            first.next = sec.next;
            cur.next = sec;
            cur.next.next = first;
            cur = cur.next.next;
        }

        return tmp.next;
    }
}
