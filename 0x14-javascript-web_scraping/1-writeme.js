#!/usr/bin/node
// writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, (err) => {
  if (err) {
    console.log(err);
  }
});
