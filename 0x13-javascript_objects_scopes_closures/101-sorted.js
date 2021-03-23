#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of
// user ids by occurrence
const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  const val = dict[key];
  if (!newdict[val]) {
    newdict[val] = [key];
  } else {
    newdict[val].push(key);
  }
}
console.log(newdict);
