#!/usr/bin/node
/**
 * a script that display the status code of a GET request.
 * first argument is the URL to request (GET)
 */
const myArgs = process.argv.slice(2);
const request = require('request');
request
  .get(myArgs[0])
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  })
  .on('error', error => {
    console.log(error);
  });
