#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(function (character) {
    request(character, function (err, response, body) {
      if (err) {
        console.error(err);
        return;
      }
      if (response.statusCode !== 200) {
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
