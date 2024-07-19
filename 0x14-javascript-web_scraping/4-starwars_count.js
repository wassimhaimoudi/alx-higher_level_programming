#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
let numberOfMovies = 0;
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    for (const result of results) {
      const characters = result.characters;
      if (characters.some(function (character, index) {
        return character.includes(`/people/${characterId}/`);
      })) {
        numberOfMovies += 1;
      }
    }
  }
  console.log(numberOfMovies);
});
