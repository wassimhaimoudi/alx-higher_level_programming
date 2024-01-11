#!/usr/bin/node
const list = require('./100-data').list;

const mapped = list.map((x, index, list) => x * index);
console.log(list);
console.log(mapped);
