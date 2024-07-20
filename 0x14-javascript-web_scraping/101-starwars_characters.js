#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
	  return;
  }
  if (response.statusCode !== 200) {
    return;
  }
  const movie = JSON.parse(body).results[movieId - 1];
  const characters = movie.characters;
  /* characters.forEach(function(character) {
		request(character, function(err, response, body) {
			if (err) {
				throw err;
			}
			if (response.statusCode !== 200) {
				return;
			}
			console.log(JSON.parse(body).name);
		});
*/
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (err, response, body) {
      if (err) {
        console.error(err);
	      return;
      }
      if (response.statusCode !== 200) {
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
