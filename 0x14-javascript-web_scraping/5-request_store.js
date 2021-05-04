#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (error, response, data) => {
  if (error) console.log(error);
  else {
    fs.writeFile(fileName, data, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
