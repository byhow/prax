function gcdOfStrings(str1: string, str2: string): string {
  if (str1.concat(str2) !== str2.concat(str1)) {
    return '';
  }
  return str1.substring(0, gcd(str1.length, str2.length));
}

function gcd(a: number, b: number) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}
