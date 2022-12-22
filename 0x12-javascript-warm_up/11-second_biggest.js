#!/usr/bin/node

const entry = process.argv;
const toOrder = [];
let check;

function secBig () {
  const x = toOrder.length;
  toOrder.sort(function (a, b) { return a - b; });
  console.log(toOrder[x - 2]);
}

if (entry.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < entry.length; i++) {
    check = parseInt(entry[i]);
    if (isNaN(check)) {
      continue;
    } else {
      toOrder.push(check);
    }
  }
  secBig();
}
