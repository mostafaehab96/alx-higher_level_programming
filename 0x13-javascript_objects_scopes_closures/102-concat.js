#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const first = args[2];
const second = args[3];
const third = args[4];

let firstData = '';
let secondData = '';

fs.readFile(first, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  firstData = data;

  fs.readFile(second, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    secondData = data;

    const allData = firstData + secondData;

    fs.writeFile(third, allData, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
});
