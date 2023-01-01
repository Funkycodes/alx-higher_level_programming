#!/usr/bin/node

const request = require('request');
const args = process.argv;
request(args[2], function (err, response, body) {
  if (err) throw err;
  const json = JSON.parse(body);
  const dict = {};
  json.forEach(element => {
    if (element.completed) {
      if (dict[element.userId]) {
        dict[element.userId] += 1;
      } else {
        dict[element.userId] = 1;
      }
    }
  });
  console.log(dict);
});
