#!/usr/bin/node
// a function that increments and calls a function
exports.addMeMaybe = function (x, theFunction) {
  theFunction(x + 1);
};
