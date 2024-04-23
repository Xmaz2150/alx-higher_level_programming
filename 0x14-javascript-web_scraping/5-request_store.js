#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const argv = process.argv;

request(`${argv[2]}/`, function (err, response, body) {
  if (err) {
    console.error(err);
  }

  fs.writeFile(`${argv[3]}`, body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
