#!/usr/bin/node

exports.esrever = function (list) {
  if (!list) {
    return (null);
  }

  let len = Math.floor(list.length) - 1;
  for (let i = 0; i <= len; i++) {
    const backIdx = len--;
    const temp = list[i];

    list[i] = list[backIdx];
    list[backIdx] = temp;
  }

  return (list);
};
