#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  for (const i in list) {
    if (list[i] === searchElement) oc++;
  }
  return oc;
};
