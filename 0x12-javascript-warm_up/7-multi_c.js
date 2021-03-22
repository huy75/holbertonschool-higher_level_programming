#!/usr/bin/node
// Prints x times 'C is fun'

if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else if (process.argv[2] > 0) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
