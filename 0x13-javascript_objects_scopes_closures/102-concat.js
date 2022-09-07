#!/usr/bin/node
const fs = require('fs'); // file system
function fileread (filename) {
  return fs.readFileSync(filename);
}
const fileA = fileread(process.argv[2]).toString();
const fileB = fileread(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fileA + fileB);
