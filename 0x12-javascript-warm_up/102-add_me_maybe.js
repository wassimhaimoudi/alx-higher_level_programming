#!/usr/bin/node

exports.addMeMaybe = function addMeMaybe (number, thisFunction) {
  number++;
  thisFunction(number);
};
