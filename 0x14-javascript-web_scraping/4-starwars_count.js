#!/usr/bin/node

const request = require('request');
const argv = process.argv;

request(`${argv[2]}/`, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const filmsList = JSON.parse(body).results;
  const actorId = '18';
  let idCount = 0;
  for (let i = 0; i < filmsList.length; i++) {
    for (let j = 0; j < filmsList[i].characters.length; j++) {
      const id = filmsList[i].characters[j].match(/\d+/);
      if (actorId === id + '') {
        idCount++;
      }
    }
  }
  console.log(`${idCount}`);
});
