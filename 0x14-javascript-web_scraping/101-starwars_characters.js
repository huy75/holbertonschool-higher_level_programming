#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first argument is the Movie ID
 * in the same order of the list characters in the /films/ response
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
/*
request.get(url, (error, response, data) => {
  if (error) console.log(error);
  else {
    const film = JSON.parse(data);
    const characters = film.characters;
    let idx;

    for (idx = 0; idx < characters.length; idx++) {
      request(characters[idx], (error, response, data) => {
        if (error) console.log(error);
        else {
          const chars = JSON.parse(data);
          console.log(chars.name);
        }
      });
    }
  }
});
*/

request.get(url, (error, response, data) => {
  if (error) console.log(error);
  else {
    const character = JSON.parse(data).characters;
    printcur(character, 0);
  }
});

function printcur (arr, idx) {
  if (idx >= arr.length) {
    return;
  }
  request.get(arr[idx], (e, r, b) => {
    if (e) console.log(e);
    else {
      console.log(JSON.parse(b).name);
    }
    return printcur(arr, idx + 1);
  });
}
