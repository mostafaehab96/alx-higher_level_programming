#!/usr/bin/node

const args = process.argv;
const url = args[2];
const request = require('request');

if (url) {
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    if (response) {
      let count = 0;
      const results = JSON.parse(body).results;
      for (const result of results) {
        const characters = result.characters;
        for (const character of characters) {
          if (character.slice(-3, -1) === '18') {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
