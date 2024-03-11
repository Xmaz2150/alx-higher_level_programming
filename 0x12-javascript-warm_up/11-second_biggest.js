#!/usr/bin/node

const argv = process.argv;

function toInt (a) {
  return parseInt(a);
}

const argC = argv.length - 2;
if (argC === 0 || argC === 1) {
  console.log(0);
} else {
  const args = argv.slice(2);
  const cleanList = args.map(toInt).sort();

  console.log(cleanList[argC - 2]);
}
