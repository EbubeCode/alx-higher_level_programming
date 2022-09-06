#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((e, i) => e * i);
console.log(list);
console.log(newList);
