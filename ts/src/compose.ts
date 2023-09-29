type F = (x: number) => number;

function compose(functions: F[]): F {
  return (x) => functions.reduceRight((curr, next) => next(curr), x);
}

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
