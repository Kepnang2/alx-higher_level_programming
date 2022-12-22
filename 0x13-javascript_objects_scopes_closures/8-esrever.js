#!/usr/bin/node

exports.esrever = function (list) {
  let i; const reversed = []; let current;
  for (i = list.length - 1; i >= 0; i--) {
    current = list.pop();
    reversed.push(current);
  }
  return (reversed);
};
