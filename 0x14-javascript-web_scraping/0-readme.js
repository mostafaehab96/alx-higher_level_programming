#!/usr/bin/node

const args = process.argv;
const path = args[2] ? args[2] : '';
const fs = require('fs');

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
