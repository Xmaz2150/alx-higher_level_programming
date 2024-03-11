#!/usr/bin/node

function printLanguagesMessageLoop () {
  const firstArg = process.argv[2];
  const firstArgInt = parseInt(firstArg);

  if (!firstArg) {
    console.log('Missing number of occurrences');
    return;
  } else if (!firstArgInt || firstArgInt < 0) {
    return;
  }
  for (let i = 0; i < firstArgInt; i++) {
    console.log('C is fun');
  }
}

printLanguagesMessageLoop();
