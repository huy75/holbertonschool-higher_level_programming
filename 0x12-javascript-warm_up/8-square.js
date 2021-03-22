#!/usr/bin/node
// prints a square
const size = parseInt(process.argv[2]);
let idx;

if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (idx = 0; idx < size; idx++) {
    console.log('X'.repeat(size));
  }
}
