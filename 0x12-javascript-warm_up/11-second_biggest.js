#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const arr = process.argv;
  const slicedArray = arr.slice(2);
  const sortedArray = slicedArray.sort((a, b) => a - b);
  const reversedArray = sortedArray.reverse();
  console.log(reversedArray[1]);
