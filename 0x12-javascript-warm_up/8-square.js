#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
if (!isNaN(num)) {
  for (let i = 1; i <= num; i++) {
    let s = '';
    for (let j = 1; j <= num; j++) {
      s += 'X';
    }
    console.log(s);
  }
} else {
  console.log('Missing size');
}
