#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let x = 0;
  while (x < size) {
    console.log('X'.repeat(size));
    x++;
  }
}
