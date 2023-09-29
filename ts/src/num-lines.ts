function numberOfLines(widths: number[], s: string): number[] {
  if (widths.length !== 26) {
    return [-1, -1];
  }
  let alphabet: Record<string, number> = {};
  let curr = 0;
  let [lines, remain] = [0, 0];
  for (const char of 'abcdefghijklmnopqrstuvwxyz') {
    alphabet[char] = widths[curr];
    curr++;
  }
  for (const c of s) {
    if (remain + alphabet[c] <= 100) {
      remain += alphabet[c];
    } else {
      lines++;
      remain = alphabet[c];
    }
  }
  return [lines + 1, remain];
}
