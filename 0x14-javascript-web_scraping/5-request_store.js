#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, 'utf8', (fileError) => {
    if (fileError) {
      console.log(fileError);
    }
  });
});
