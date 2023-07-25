#!/usr/bin/node

const args = process.argv;
const url = args[2];
const path = args[3];
const request = require('request');
const fs = require('fs');

if (url && path) {
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    if (response) {
      fs.writeFile(path, body, (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
