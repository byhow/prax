package com.acme;

public class MergeLL {
//      Definition for singly-linked list.
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null;
        ListNode ret = new ListNode(0);
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                ret.val = l1.val;
                l1 = l1.next;
            } else {
                ret.val = l2.val;
                l2 = l2.next;
            }
        }

        if (l1 == null) {
            ret.val = l2.val;
            ret.next = l2.next;
        } else {
            ret.val = l1.val;
            ret.next = l1.next;
        }

        return ret;
    }

}
