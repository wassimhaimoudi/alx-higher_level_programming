#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
for (let x = 0; x < process.argv[2]; x++) {
  console.log('C is fun');
}
