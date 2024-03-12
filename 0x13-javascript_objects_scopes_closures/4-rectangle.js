#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number') {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (!c) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      console.log('');
    }
  }

  rotate () {
    this.temp = this.width;
    this.width = this.height;
    this.height = this.temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
