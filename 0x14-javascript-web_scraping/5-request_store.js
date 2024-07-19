#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }
  fs.writeFile(fileName, body, function (err) {
    if (err) {
      console.error(err);
    }
  });
});
