#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const i in dict) {
  const v = dict[i];
  if (newDict[v]) {
    newDict[v].push(i);
  } else {
    newDict[v] = [i];
  }
}
console.log(newDict);
