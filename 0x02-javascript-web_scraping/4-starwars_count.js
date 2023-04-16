#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const arg_ = argv[2];
const url = arg_;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  let count = 0;
  const json_ = JSON.parse(body).results;
  for (const property of json_) {
    for (const property2 of property.characters) {
      if (property2.includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
