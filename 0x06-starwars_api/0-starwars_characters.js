#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log("Please provide a Movie ID as a positional argument.");
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch the movie details based on the provided movie ID
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // For each character URL, fetch and print the character name
    characterUrls.forEach((url) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.log(`Error: Unable to retrieve movie with ID ${movieId}.`);
  }
});
