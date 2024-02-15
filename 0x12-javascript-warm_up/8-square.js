#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let x = 0;
  let s = '';
  while (x < size) {
    let y = 0;
    while (y < size) {
      s += 'X';
      y++;
    }
    s += '\n';
    x++;
  }
  console.log(s);
}
