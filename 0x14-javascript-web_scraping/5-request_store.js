#!/usr/bin/node

const fs = require('fs');
const req = require('request');

req(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) console.log(err);
    });
  }
});
