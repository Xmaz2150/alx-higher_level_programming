#!/usr/bin/node

const argv = process.argv;

function factorial (n) {
  if (n === 0 || n === 1 || n < 0) {
    return (1);
  }
  return n * factorial(n - 1);
}

const num = argv[2];
console.log(factorial(num));
