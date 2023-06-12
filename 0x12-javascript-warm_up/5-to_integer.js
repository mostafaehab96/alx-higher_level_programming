#!/usr/bin/node

const args = process.argv;
const first = args[2];
const parsedFirst = parseInt(first);

if (parsedFirst) {
  console.log(`My number: ${parsedFirst}`);
} else {
  console.log('Not a number');
}
