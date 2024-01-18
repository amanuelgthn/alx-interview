#!/usr/bin/node
/*
script that prints all characters of a star war movie
 The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 You must use the Star wars API
 You must use the request module
*/

const request = require('request');

if (!process.argv[2]) {
  return
}
const position = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + position + '/';
request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const jsonData = JSON.stringify(response);
    const jsonNew = JSON.parse(jsonData);
    const jsonBody = JSON.parse(jsonNew.body);
    for (let i = 0; i < jsonBody.characters.length; i++) {
      request(jsonBody.characters[i], (err, responseN) => {
        if (err) {
          console.log(err);
        } else {
          const jsonName = JSON.stringify(responseN);
          const jsonValue = JSON.parse(jsonName);
          const jsonFinal = JSON.parse(jsonValue.body);
          console.log(jsonFinal.name);
        }
      });
    }
  }
});