#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

fs.readFile(`${argv[2]}`, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
