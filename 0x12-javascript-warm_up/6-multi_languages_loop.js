#!/usr/bin/node

function printLanguagesMessageLoop () {
  const lans = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

  for (let i = 0; i < lans.length; i++) {
    console.log(lans[i]);
  }
}

printLanguagesMessageLoop();
