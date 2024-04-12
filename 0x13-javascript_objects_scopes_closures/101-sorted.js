#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
const listKeys = [];

for (const x in dict) {
  if (!(listKeys.includes(dict[x]))) {
    listKeys.push(dict[x]);
  }
}

const sortedKeys = listKeys.sort((a, b) => a - b);

for (const x of sortedKeys) {
  newDict[x] = [];
  for (const y in dict) {
    if (dict[y] === x) {
      newDict[x].push(y);
    }
  }
}

console.log(newDict);
