// a list of bid
const exampleOrderBook = {
  // 1. this is decreasing price

  bids: [
    { price: 10.0, quantity: 0.3 },
    { price: 9.5, quantity: 2.9 },
    { price: 9.0, quantity: 0.1 },
    { price: 8.5, quantity: 1.2 },
  ],

  // 1. this is increasing price
  asks: [
    { price: 10.5, quantity: 2.4 },
    { price: 11.0, quantity: 1.4 },
    { price: 11.5, quantity: 1.3 },
    { price: 12.0, quantity: 0.9 },
  ],

  // bids and asks do not cross
  // remaining orders that needs to be made, so they'd never overlaps
};

// 1. match the best price first
// 2. fill the quantity portion of the next price
// 3. if quantity > all combined, will just need to empty orderbook
// 4. potentially has average price calc
const exampleMarketBuyOrSells = {};

type Config = {
  // startPrice: number;
  // endPrice: number;
  startQuantity: number;
  endQuantity: number;
  // numberOfEntries: number; // TODO: make it a range as well
};

type Entry = {
  price: number;
  quantity: number;
};
function generateFakeOrderBook({ startQuantity, endQuantity }: Config) {
  const [bids, asks]: Entry[][] = [[], []];
  let startBids = 9;
  let startAsks = 9;
  for (let i = 0; i < 4; i++) {
    // endprice - startprice / numberof entries
    bids.push({
      price: startBids - 0.5,
      quantity: between(startQuantity, endQuantity),
    });
    startBids -= 0.5;
  }

  for (let i = 0; i < 4; i++) {
    // endprice - startprice / numberof entries
    asks.push({
      price: startAsks + 0.5,
      quantity: between(startQuantity, endQuantity),
    });
    startAsks += 0.5;
  }

  return {
    bids,
    asks,
  };
}

function between(min: number, max: number) {
  return Math.trunc(Math.random() * (max - min) + min);
}

console.log(
  generateFakeOrderBook({
    startQuantity: 1,
    endQuantity: 4,
  }),
);

// 1. sell a fixed quantity of assets
// 2. get the net revenue from this particular order
// 3. after the sale is complete, the average of the order filled
//     total price you paid / quantity
// 4. the returned oreder book
function marketSell(orderBook: typeof exampleOrderBook, quantity: number) {
  // if selling, go from highest
  // bids - how much people want to buy
  let remainingQuantity = quantity;
  let curr = 0;
  let revenue = 0;

  while (remainingQuantity > 0 && curr < orderBook.bids.length) {
    const currPrice = orderBook.bids[curr].price;
    const currQuantity = orderBook.bids[curr].quantity;
    // price 10, quantity 0.2; curr is 0.3
    if (remainingQuantity < currQuantity && orderBook.bids.length > 0) {
      revenue += currPrice * remainingQuantity;
      const entry = orderBook.bids.shift();
      // TODO: check if array is empty
      orderBook.bids.unshift({
        price: entry?.price!,
        quantity: currQuantity - remainingQuantity,
      });
      break;
    } else {
      const entry = orderBook.bids.shift();
      revenue += entry?.price! * entry?.quantity!;
      remainingQuantity -= orderBook.bids[curr].quantity;
    }
  }

  return {
    orderBook,
    avg: revenue / quantity,
    revenue,
  };
}
