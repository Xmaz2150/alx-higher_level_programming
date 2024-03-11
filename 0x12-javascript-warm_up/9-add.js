#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  const aInt = parseInt(a);
  const bInt = parseInt(b);

  return (aInt + bInt);
}

const firstArg = argv[2];
const secondArg = argv[3];
const firstArgInt = parseInt(firstArg);
const secondArgInt = parseInt(secondArg);

const sum = add(firstArgInt, secondArgInt);
console.log(sum);
