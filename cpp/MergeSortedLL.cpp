class Solution {

    struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(nullptr) {}
    };

public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) {
            return l2;
        }
        else if (!l2) {
            return l1;
        }
        
        ListNode* ret, *tmp;
        if (l1 -> val < l2 -> val) {
            tmp = new ListNode(l1 -> val);
            l1 = l1 -> next;
        } else {
            tmp = new ListNode(l2 -> val);
            l2 = l2 -> next;
        }

        ret = tmp;
        while (l1 && l2) {
            if (l1 -> val < l2 -> val) {
                tmp -> next = new ListNode(l1 -> val);                
                l1 = l1 -> next;
            } else {
                tmp -> next = new ListNode(l2 -> val);
                l2 = l2 -> next;
            }
            tmp = tmp -> next;
        }
        
        if (l1) {
            tmp -> next = l1;
        } else if (l2) {
            tmp -> next = l2;
        }
        
        
        return ret;
    }
};