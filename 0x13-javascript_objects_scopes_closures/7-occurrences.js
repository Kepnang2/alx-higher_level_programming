#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0; let item;
  for (item of list) {
    if (item === searchElement) {
      count++;
    }
  }
  return (count);
};
