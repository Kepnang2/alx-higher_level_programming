#!/usr/bin/node

const args = process.argv;

const num = parseInt(args[2]);
let i;

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
