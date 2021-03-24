#!/usr/bin/node
// Computes and prints a factorial

function fact (n) {
  if (isNaN(n) || n < 2) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
const num = parseInt(process.argv[2], 10);

console.log(fact(num));
