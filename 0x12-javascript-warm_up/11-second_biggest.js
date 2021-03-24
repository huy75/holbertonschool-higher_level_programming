#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

console.log(process.argv.length < 4 ? 0 : process.argv.slice(2).sort((a, b) => b - a)[1]);
