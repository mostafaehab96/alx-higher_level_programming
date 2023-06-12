#!/usr/bin/node

const args = process.argv;
const n = parseInt(args[2]);

if (n || n === 0) {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
