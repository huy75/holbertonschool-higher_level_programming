#!/usr/bin/node
// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let total = 0;

  list.forEach((currentItem) => {
    if (currentItem === searchElement) {
      total++;
    }
  });
  return total;
};
