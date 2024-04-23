#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(`${argv[2]}`, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${response.statusCode}`);
});
