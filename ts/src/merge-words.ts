function mergeAlternately(word1: string, word2: string): string {
  let result = '';
  let [i, j] = [0, 0]; // current pointer

  while (i < word1.length || j < word2.length) {
    if (i < word1.length) {
      result = result.concat(word1[i]);
      i += 1;
    }
    if (j < word2.length) {
      result = result.concat(word2[j]);
      j += 1;
    }
  }

  return result;
}
