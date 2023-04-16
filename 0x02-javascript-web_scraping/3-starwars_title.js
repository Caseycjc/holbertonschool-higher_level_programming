#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const arg_ = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + arg_;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const json_ = JSON.parse(body);
  console.log(json_.title);
});
