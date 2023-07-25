#!/usr/bin/node

const args = process.argv;
const url = args[2] ? args[2] : '';
const request = require('request');

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response) {
    console.log('code: ' + response.statusCode);
  }
});
