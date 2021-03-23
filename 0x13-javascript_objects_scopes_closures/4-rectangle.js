#!/usr/bin/node
// Rectangle class
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 &&
        (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const h = this.height;
    const w = this.width;
    this.width = h;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
