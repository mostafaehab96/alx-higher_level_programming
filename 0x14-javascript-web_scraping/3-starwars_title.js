#!/usr/bin/node

const args = process.argv;
const id = args[2];
const request = require('request');

if (id) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    if (response && response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  });
}
