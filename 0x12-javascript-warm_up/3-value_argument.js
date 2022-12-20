#!/usr/bin/node

const values = process.argv;

if (values[2]) {
  console.log(values[2]);
} else {
  console.log('No argument');
}
