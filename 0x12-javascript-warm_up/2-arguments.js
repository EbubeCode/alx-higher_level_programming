#!/usr/bin/node
const arglen = process.argv.length;
if (arglen === 2) {
  console.log('No argument');
} else if (arglen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
