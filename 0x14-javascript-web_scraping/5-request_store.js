#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;
let content = '';

request(args[2], function (err, response) {
  if (err) throw err;
  content = Buffer.from(response.body, 'utf-8').toString();
  fs.writeFile(args[3], content, err => {
    if (err) {
      console.error(err);
    }
  });
});
