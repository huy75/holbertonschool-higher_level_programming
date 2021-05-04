#!/usr/bin/node
// Rrads and prints contents of a file

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf8', function (err, data) {
  if (err) console.log(err);
  else process.stdout.write(data);
});
