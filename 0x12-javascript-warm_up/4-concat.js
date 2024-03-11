#!/usr/bin/node

function concatArgs () {
  const firstArg = process.argv[2];
  const secondArg = process.argv[3];

  console.log(`${firstArg} is ${secondArg}`);
}

concatArgs();
