#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) return 1;
  else return (n * factorial(n - 1));
}

const arg = process.argv[2];
const num = parseInt(arg);

console.log(factorial(num));
