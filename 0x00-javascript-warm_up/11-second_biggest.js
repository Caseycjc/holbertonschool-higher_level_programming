#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  args.splice(0, 2);
  const second = secondBiggest(args);
  console.log(second);
}

function secondBiggest (list) {
  const max = list.sort((a, b) => a - b);
  return max[max.length - 2];
}
