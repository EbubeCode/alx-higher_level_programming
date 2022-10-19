#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else {
    let number = 0;
    for (const film of JSON.parse(body).results) {
      for (const ch of film.characters) {
        if (ch.includes('18')) number++;
      }
    }
    console.log(number);
  }
});
