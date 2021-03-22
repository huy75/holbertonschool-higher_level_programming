#!/usr/bin/node
/*
Prints two arguments passed
*/
if (process.argv.length === 4) {
  console.log(process.argv[2].concat(' is ', process.argv[3]));
} else if (process.argv.length === 3) {
  console.log(process.argv[2].concat(' is ', 'undefined'));
} else if (process.argv.length <= 2) {
  console.log('undefined'.concat(' is ', 'undefined'));
}
