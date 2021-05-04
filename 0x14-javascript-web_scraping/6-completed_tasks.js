#!/usr/bin/node
// the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];
const completed = {};

request.get(url, (error, response, data) => {
  if (error) console.log(error);
  else {
    const todos = JSON.parse(data);
    for (const task of todos) {
      if (task.completed === true) {
        if (!(task.userId in completed)) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
  }
  console.log(completed);
});
