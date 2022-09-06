#!/usr/bin/node
exports.callMeMoby = function (x, theFunc) {
  for (let i = 1; i <= x; i++) theFunc();
};
