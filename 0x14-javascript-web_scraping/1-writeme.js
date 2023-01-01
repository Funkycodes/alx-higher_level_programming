#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const content = Buffer.from(args[3], 'utf-8').toString();

fs.writeFile(args[2], content, err => {
  if (err) {
    console.error(err);
  }
});
