#!/usr/bin/node

const args = process.argv;
const filename = args[2] ? args[2] : '';
const content = args[3] ? args[3] : '';
const fs = require('fs');

fs.writeFile(filename, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
