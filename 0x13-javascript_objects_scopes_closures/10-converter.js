#!/usr/bin/node
exports.converter = function (base) {
  return (x) => {
    return (x).toString(base);
  };
};
