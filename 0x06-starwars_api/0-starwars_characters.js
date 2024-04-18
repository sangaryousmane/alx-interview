#!/usr/bin/node
const argv = process.argv;
const filmUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieUrl = `${filmUrl}${argv[2]}/`;

const request = require('request');

request(movieUrl, function (error, response, body) {
  if (!error) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (characters && characters.length > 0) {
      const characterCount = characters.length;
      retrieveCharacters(0, characters[0], characters, characterCount);
    }
  } else {
    console.log(error);
  }
});

function retrieveCharacters (index, characterUrl, characters, characterCount) {
  if (index === characterCount) {
    return;
  }
  request(characterUrl, function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      index++;
      retrieveCharacters(index, characters[index], characters, characterCount);
    } else {
      console.error('Error:', error);
    }
  });
}
