#!/usr/bin/node

const BSquare = require('./5-square');

class Square extends BSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      if (typeof c === 'undefined') {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
