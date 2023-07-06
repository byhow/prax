const memoize = (f) => {
  const results = {}
  return (...args) => {
    const argsKey = JSON.stringify(args)
    if (!results[argsKey]) {
      results[argsKey] = f(args)
    }
    return results[argsKey]
  }
}

const clumsySquare = memoize(n => {
  let result = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      result++
    }
  }
  return result
})

console.info(clumsySquare(1000))
console.info(clumsySquare(3493))
console.log(clumsySquare(7467));
console.log(clumsySquare(9666));

