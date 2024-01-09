#!/usr/bin/node

const sliced = process.argv.slice(2);
if (sliced.length === 0 || sliced.length === 1) {
  console.log(0);
} else {
  sliced.sort((a, b) => a - b);
  sliced.reverse();
  const secondLargest = sliced[1];
  console.log(secondLargest);
}
