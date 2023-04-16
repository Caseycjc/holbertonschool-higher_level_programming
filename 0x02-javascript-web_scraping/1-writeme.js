#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const data_ = new Uint8Array(Buffer.from(argv[3]));
fs.writeFile(process.argv[2], data_, function (err, data) {
  if (err) {
    return console.log(err);
  }
});
