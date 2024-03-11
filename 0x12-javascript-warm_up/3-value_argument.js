#!/usr/bin/node

function firstArgs () {
  const firstArg = process.argv[2];

  if (!firstArg) {
    console.log('No argument');
    return;
  }
  console.log(`${firstArg}`);
}

firstArgs();
