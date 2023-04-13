#!/usr/bin/node
const fs = require('fs');

function readAndPrintFile (filePath) {
  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      console.error('An error occurred:', error);
    } else {
      console.log(data);
    }
  });
}

if (process.argv.length > 2) {
  const filePath = process.argv[2];
  readAndPrintFile(filePath);
} else {
  console.error('Please provide a file path as an argument');
}
