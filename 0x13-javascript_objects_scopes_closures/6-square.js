#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c) {
      let line = '';
      for (let i = 0; i < this.height; i++) {
        line = '';
        for (let j = 0; j < this.width; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
