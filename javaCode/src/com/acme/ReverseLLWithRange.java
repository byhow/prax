package com.acme;

public class ReverseLLWithRange {
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) return head;

        ListNode ret = new ListNode(0);
        ret.next = head;

        ListNode prev = ret;
        for (int i = 1; i < m; i++) prev = prev.next;

        ListNode start = prev.next;
        ListNode then = start.next;

        for (int i = 0; i < n - m; i++) {
            start.next = then.next;
            then.next = prev.next;
            prev.next = then;
            then = start.next;
        }

        return ret.next;

    }
}
