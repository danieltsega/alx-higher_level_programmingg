#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.statusMessage);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
