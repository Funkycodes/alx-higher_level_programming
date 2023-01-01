#!/usr/bin/node

/* File System Object */
const fs = require('fs');
const args = process.argv;

/* Read File */
fs.readFile(args[2], bar);

function bar (err, data) {
  /* If an error exists, show it, otherwise show the file */
  err ? console.log(err) : console.log(String(data));
}
