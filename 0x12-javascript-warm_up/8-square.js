#!/usr/bin/node

function printLanguagesMessageLoop () {
  const firstArg = process.argv[2];
  const firstArgInt = parseInt(firstArg);

  if (!firstArg || !firstArgInt) {
    console.log('Missing size');
    return;
  } else if (firstArgInt < 0) {
    return;
  }
  for (let i = 0; i < firstArgInt; i++) {
    for (let j = 0; j < firstArgInt; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}

printLanguagesMessageLoop();
