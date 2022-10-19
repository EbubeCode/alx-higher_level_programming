#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else console.log('code:', response && response.statusCode);
});
