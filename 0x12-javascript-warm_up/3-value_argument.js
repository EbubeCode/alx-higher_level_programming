#!/usr/bin/node
let len = 0;
for (const x in process.argv) {
  if (x === undefined) {
    console.log(x);
  }
  len++;
}
if (len === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2])
}
