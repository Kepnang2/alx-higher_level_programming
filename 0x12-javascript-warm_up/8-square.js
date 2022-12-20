#!/usr/bin/node

const args = process.argv;

const num = parseInt(args[2]);
let i, j;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    for (j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
