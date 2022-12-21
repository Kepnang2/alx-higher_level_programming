#!/usr/bin/node

const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    let i;
    for (i = 0; i < this.width; i++) {
      if (c) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
