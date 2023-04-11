#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
console.log(factorial(args[2]));
