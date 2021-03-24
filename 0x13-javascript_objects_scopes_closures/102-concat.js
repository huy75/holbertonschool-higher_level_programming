#!/usr/bin/node
// a script that concats 2 files.

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fs = require('fs');
const a = fs.readFileSync(fileA, 'utf8');
const b = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(fileC, a + b);
