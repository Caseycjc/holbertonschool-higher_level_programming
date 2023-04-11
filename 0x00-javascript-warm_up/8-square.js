#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
