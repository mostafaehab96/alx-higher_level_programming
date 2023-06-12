#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);
let line;

if (size || size === 0) {
  for (let i = 0; i < size; i++) {
    line = [];
    for (let j = 0; j < size; j++) {
      line.push('X');
    }
    console.log(line.join(''));
  }
} else {
  console.log('Missing size');
}
