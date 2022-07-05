/**
 * Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
 * 
 * Implement the LRUCache class:

 * LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
 * int get(int key) Return the value of the key if the key exists, otherwise return -1.
 * void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
 * The functions get and put must each run in O(1) average time complexity.
 * 
 * Hashmap hardly work as it is unordered. Probably use a linked list
 */

interface LRUNode {
  key: number;
  val: number;
  prev: LRUNode;
  next: LRUNode;
}

class LRUCache {
  #head = <LRUNode>{};
  #tail = <LRUNode>{};
  #nodeMap = <Record<number, LRUNode>>{};
  #size = 0; // hashmap's size

  constructor(private capacity: number) {
    // need to evict the old cache
    this.#head.next = this.#tail;
    this.#tail.prev = this.#head;
  }

  get(key: number): number {
    let res = -1;
    const node = this.#nodeMap[key];
    if (node) {
      res = node.val;
      this.pop(node);
      this.unshift(node);
    }
    return res;
  }

  put(key: number, value: number): void {
    const node = this.#nodeMap[key];
    if (node) {
      this.pop(node);
      node.val = value;
      this.unshift(node);
    } else {
      if (this.#size === this.capacity) {
        delete this.#nodeMap[this.#tail.prev.key];
        this.pop(this.#tail.prev);
      }
      const newNode: LRUNode = {
        key,
        val: value,
        prev: <LRUNode>{},
        next: <LRUNode>{},
      };
      this.#nodeMap[key] = newNode;
      this.unshift(newNode);
    }
  }

  unshift(node: LRUNode): void {
    const headNext = this.#head.next;
    node.next = headNext;
    headNext.prev = node;
    this.#head.next = node;
    node.prev = this.#head;
    this.#size++;
  }

  pop(node: LRUNode) {
    const nextNode = node.next;
    const prevNode = node.prev;
    nextNode.prev = prevNode;
    prevNode.next = nextNode;
    this.#size--;
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
