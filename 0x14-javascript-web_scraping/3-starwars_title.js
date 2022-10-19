#!/usr/bin/node

const req = require('request');

req(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (err, response, body) {
  if (err) console.log(err);
  else console.log(JSON.parse(body).title);
});
