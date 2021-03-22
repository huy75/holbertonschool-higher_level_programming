#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

const args = process.argv;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let idx;
  for (idx = 0; idx < process.argv.length; idx++) {
    args[idx] = parseInt(process.argv[idx]);
  }
  // eliminate duplicates
  // const newA = Array.from([...new Set(args)]);
  console.log(args.slice(2).sort(function (a, b) { return b - a; })[1]);
}
