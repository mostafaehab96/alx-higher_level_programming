#!/usr/bin/node

const dict = require('./101-data').dict;

const entries = Object.entries(dict);
const values = new Set(Object.values(dict));
const newDict = {};

for (const value of values) {
  newDict[value] = [];
  for (const entry of entries) {
    if (entry[1] === value) newDict[value].push(entry[0]);
  }
}

console.log(newDict);
