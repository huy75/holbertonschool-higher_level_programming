#!/usr/bin/node
// prints all characters of a Star Wars movie
// The first argument is the Movie ID

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, data) => {
  if (error) console.log(error);
  else {
    const film = JSON.parse(data);
    const characters = film.characters;
    for (const character of characters) {
      request(character, (error, response, data) => {
        if (error) console.log(error);
        else {
          const chars = JSON.parse(data);
          console.log(chars.name);
        }
      });
    }
  }
});
