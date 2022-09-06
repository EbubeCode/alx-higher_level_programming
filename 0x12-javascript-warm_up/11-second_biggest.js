#!/usr/bin/node
function findSecondMax (array) {
  if (array.length <= 1) return 0;

  let m = 0;
  let x = 0;
  for (let i = 0; i < array.length; i++) {
    const y = parseInt(array[i]);
    if (m < y) {
      x = m;
      m = y;
    } else if (x < y) x = y;
  }
  return x;
}

const args = process.argv.slice(2);
console.log(findSecondMax(args));
