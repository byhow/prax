class ListNode{
    val: number;
    next: ListNode | null;
    constructor(val: number, next=null) {
        this.val = val;
        this.next = next
    }
}

class MyCircularQueue {
    maxSize: number;
    size: number;
    head: ListNode | null;
    tail: ListNode | null;
    constructor(k: number) {
        this.maxSize = k
        this.size = 0
        this.head = null
        this.tail = null
    }

    enQueue(value: number): boolean {
        if (this.isFull()) {
            return false
        }
        let newVal = new ListNode(value)
        if (this.isEmpty()) {
            this.head = this.tail = newVal
        } else {
            if (this.tail) {
                this.tail.next = newVal
                this.tail = this.tail?.next
            }
        }
        this.size++
        return true
        
    }

    deQueue(): boolean {
        if (this.isEmpty()) {
            return false
        } 
        if (this.head) {
            this.head = this.head.next
        }
        
        this.size--
        return true
    }

    Front(): number {
        return this.isEmpty() ? -1 : this.head ? this.head.val : -1
    }

    Rear(): number {
        return this.isEmpty() ? -1 : this.tail ? this.tail.val : -1
    }

    isEmpty(): boolean {
        return (this.size === 0)
    }

    isFull(): boolean {
        return (this.size === this.maxSize)
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */
