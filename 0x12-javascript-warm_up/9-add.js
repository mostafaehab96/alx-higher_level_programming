#!/usr/bin/node

const args = process.argv;
console.log(add(parseInt(args[2]), parseInt(args[3])));

function add (a, b) {
  return a + b;
}
