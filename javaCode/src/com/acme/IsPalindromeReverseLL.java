package com.acme;

public class IsPalindromeReverseLL {
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head, slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        if(fast!=null){
            slow=slow.next;
        }
        slow = reverse(slow);

        fast = head;

        while(slow!=null){
            if(fast.val != slow.val){
                return false;
            }
            fast=fast.next;
            slow=slow.next;

        }
        return true;
    }

    public ListNode reverse(ListNode head) {
        ListNode ret = null;

        while (head != null) {
            ListNode tmp = head.next;
            head.next = ret;
            ret = head;
            head = tmp;
        }

        return ret;
    }
}
