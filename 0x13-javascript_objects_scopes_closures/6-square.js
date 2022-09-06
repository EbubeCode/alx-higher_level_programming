#!/usr/bin/node
const Squar = require('./5-square');
module.exports = class Square extends Squar {
  charPrint (c) {
    if (c) {
      for (let i = 1; i <= this.height; i++) {
        let s = '';
        for (let j = 1; j <= this.width; j++) {
          s += c;
        }
        console.log(s);
      }
    } else {
      super.print();
    }
  }
};
