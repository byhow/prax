package com.acme;

public class ReverseLL {
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }


    public ListNode reverseList(ListNode head) {
        if (head == null) return null;

        ListNode nex = head.next;
        if (nex == null) return head;

        ListNode ret = reverseList(head.next);

        nex.next = head;
        head.next = null;

        return ret;

    }
}
