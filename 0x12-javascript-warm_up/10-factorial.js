#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2]);

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  }
  let fact;
  fact = n;
  fact *= factorial(n - 1);
  return (fact);
}

console.log(factorial(num));
