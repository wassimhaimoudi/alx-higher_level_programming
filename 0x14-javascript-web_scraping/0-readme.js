#!/usr/bin/node

const fs = require('fs');

fs.readFileSync(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
  }
});
