#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const fs = require('fs');

const url = argv[2];
const destinyFile = argv[3];
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(destinyFile, body, 'utf8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
