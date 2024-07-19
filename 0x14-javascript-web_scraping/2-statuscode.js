#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
