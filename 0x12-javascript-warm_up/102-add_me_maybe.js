#!/usr/bin/node

exports.addMeMaybe = function (nb, theFunction) {
  nb++;
  theFunction(nb);
};
