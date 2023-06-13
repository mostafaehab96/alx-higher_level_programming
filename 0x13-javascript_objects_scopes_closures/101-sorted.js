#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
let value;

for (const key in dict) {
  value = dict[key];
  if (!newDict[value]) newDict[value] = [];
  newDict[value].push(key);
}

console.log(newDict);
