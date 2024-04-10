#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const x of list) {
    if (x === searchElement) { counter++; }
  }
  return counter;
};
