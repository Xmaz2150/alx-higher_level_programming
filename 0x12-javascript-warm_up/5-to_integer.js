#!/usr/bin/node

function myToInt () {
  const firstArg = process.argv[2];
  const firstArgInt = parseInt(firstArg);

  if (!firstArgInt) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${firstArg}`);
  }
}

myToInt();
