#!/usr/bin/node

function helloArgs () {
  const argC = process.argv.length - 2;

  if (argC === 0) {
    console.log('No argument');
  } else if (argC === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}

helloArgs();
