#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`,
  async (err, response, body) => {
    if (err) {
      console.error(err);
    } else {
      const characters = JSON.parse(body).characters;

      for (const char of characters) {
        const charName = await new Promise((resolve, reject) => {
          request.get(char, (err, response, body) => {
            if (err) {
              console.error(err);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        });
        console.log(charName);
      }
    }
  });
