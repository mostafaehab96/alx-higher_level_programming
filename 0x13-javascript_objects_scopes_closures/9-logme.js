#!/usr/bin/node

let f;
exports.logMe = function (item) {
  let logsCount = 0;

  if (!f) {
    f = function (s) {
      console.log(`${logsCount}: ${s}`);
      logsCount++;
    };
  }

  f(item);
};
