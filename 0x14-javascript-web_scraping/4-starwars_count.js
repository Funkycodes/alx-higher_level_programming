#!/usr/bin/node

const args = process.argv;
const request = require('request');
let count = 0;
request(args[2], function (err, request) {
  if (err) {
    console.error(err);
    return;
  }
  const json = JSON.parse(request.body);
  json.results.forEach(element => {
    element.characters.forEach(context => {
      const textUrl = context;
      if (textUrl.indexOf('18') !== -1) { count++; }
    });
  });
  console.log(count);
});
