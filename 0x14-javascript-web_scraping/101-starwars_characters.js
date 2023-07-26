#!/usr/bin/node

const args = process.argv;
const id = args[2];
const request = require('request');

if (id) {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
  request.get(url, async (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const characters = JSON.parse(body).characters;
      for (const url of characters) {
        const name = await new Promise((resolve, reject) => {
          request.get(url, (err, response, body) => {
            if (err) reject(err);
            else {
              resolve(JSON.parse(body).name);
            }
          });
        });
        console.log(name);
      }
    }
  });
}
