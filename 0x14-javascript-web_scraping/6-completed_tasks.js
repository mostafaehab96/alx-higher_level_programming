#!/usr/bin/node

const args = process.argv;
const url = args[2];
const request = require('request');

if (url) {
  request(url, (err, response, body) => {
    if (err) {
    // Do nothing
    }
    if (response) {
      try {
        const todos = JSON.parse(body);
        const completed = {};
        for (const todo of todos) {
          if (todo.completed) {
            completed[todo.userId] = completed[todo.userId] ? ++completed[todo.userId] : 1;
          }
        }
        if (completed) {
          console.log(completed);
        }
      } catch (error) {
        // Do nothing
      }
    }
  });
}
