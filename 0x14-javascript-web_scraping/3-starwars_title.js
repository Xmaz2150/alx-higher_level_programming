#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  console.log(`${JSON.parse(body).title}`);
});
