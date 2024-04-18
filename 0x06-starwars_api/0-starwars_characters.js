#!/usr/bin/node

const request = require('request');

function fetchMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;
      characters.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.log('Error fetching character data');
          }
        });
      });
    } else {
      console.log('Error fetching movie data');
    }
  });
}

const movieId = process.argv[2];

fetchMovieCharacters(movieId);
