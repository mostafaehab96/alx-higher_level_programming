#!/usr/bin/node

const n = parseInt(process.argv[2]);
console.log(factorial(n));

function factorial (n) {
  if (!n || n <= 1) return 1;

  return factorial(n - 1) * n;
}
