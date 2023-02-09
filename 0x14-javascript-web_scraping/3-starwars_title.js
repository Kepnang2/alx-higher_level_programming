#!/usr/bin/node
// prints the title of a Star Wars movie

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + id, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
