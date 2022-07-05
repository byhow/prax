class TrieNode {
  children: Map<string, TrieNode>;
  isTheEnd: boolean;

  constructor() {
    this.children = new Map<string, TrieNode>();
    this.isTheEnd = false;
  }
}

class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string): void {
    let cur = this.root;

    for (let i = 0; i < word.length; i++) {
      if (!cur.children.has(word[i])) {
        cur.children.set(word[i], new TrieNode());
      }
      cur = cur.children.get(word[i]) || new TrieNode();
    }
    cur.isTheEnd = true;
  }

  search(word: string): boolean {
    let cur = this.root;
    for (let i = 0; i < word.length; i++) {
      if (!cur.children.has(word[i])) {
        return false;
      }
      cur = cur.children.get(word[i]) || new TrieNode();
    }

    return cur.isTheEnd;
  }

  startsWith(prefix: string): boolean {
    let cur = this.root;
    for (let i = 0; i < prefix.length; i++) {
      if (!cur.children.has(prefix[i])) {
        return false;
      }
      cur = cur.children.get(prefix[i]) || new TrieNode();
    }
    return true;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
