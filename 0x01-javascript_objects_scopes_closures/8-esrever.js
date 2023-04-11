#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  while (list.length) {
    reverse.push(list.pop());
  }
  return reverse;
};
