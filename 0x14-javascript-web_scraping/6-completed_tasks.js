#!/usr/bin/node

const req = require('request');

req(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else {
    const complete = {};
    for (const task of JSON.parse(body)) {
      const id = task.userId;
      if (task.completed) {
        if (complete[id] !== undefined) {
          complete[id] += 1;
        } else {
          complete[id] = 1;
        }
      }
    }
    console.log(complete);
  }
});
