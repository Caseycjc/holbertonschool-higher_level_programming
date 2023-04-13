#!/usr/bin/node
const fs = require('fs');

function writeStringToFile (filePath, stringToWrite) {
  fs.writeFile(filePath, stringToWrite, 'utf8', (error) => {
    if (error) {
      console.error('An error occurred:', error);
    } else {
      console.log(`Successfully wrote to file: ${filePath}`);
    }
  });
}

if (process.argv.length > 3) {
  const filePath = process.argv[2];
  const stringToWrite = process.argv[3];
  writeStringToFile(filePath, stringToWrite);
} else {
  console.error('Please provide a file path and a string to write as arguments');
}
