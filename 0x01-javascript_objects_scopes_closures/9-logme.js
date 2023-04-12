#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(`${count}: ${item}`);
    count++;
  }
};
