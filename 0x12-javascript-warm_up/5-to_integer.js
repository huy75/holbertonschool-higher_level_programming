#!/usr/bin/node
/*
Prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
if (process.argv.length === 3) {
  const arg = parseInt(process.argv[2], 10);
  if (isNaN(arg)) {
    console.log('Not a number');
  } else {
    console.log('My number: '.concat(arg));
  }
} else {
  console.log('Not a number');
}
