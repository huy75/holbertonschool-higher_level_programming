#!/usr/bin/node
// prints the number of movies
// where the character Wedge Antilles is present.

const request = require('request');
const url = process.argv[2];

let count = 0;
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
