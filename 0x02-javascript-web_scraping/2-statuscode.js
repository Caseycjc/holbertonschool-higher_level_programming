#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const arg_ = argv[2];
request(arg_, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code:', response && response.statusCode);
});
