#!/usr/bin/node

exports.converter = function (base) {
  function myConvert (n) {
    return n.toString(base);
  }

  return myConvert;
};
