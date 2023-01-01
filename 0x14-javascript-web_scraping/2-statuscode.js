#!/usr/bin/node

const args = process.argv;
const request = require('request');
request(args[2], function (err, response) {
  if (err) throw err;
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
