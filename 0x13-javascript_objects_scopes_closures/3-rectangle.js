#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      let s = '';
      for (let j = 1; j <= this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
};
