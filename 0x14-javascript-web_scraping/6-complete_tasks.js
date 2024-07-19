#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode !== 200) {
    return;
  }

  const toDos = JSON.parse(body);
  const doneTasks = toDos.filter(toDo => toDo.completed);
  const usersCompleted = {};

  doneTasks.forEach(function (doneTask) {
    if (usersCompleted[`${doneTask.userId}`]) {
      usersCompleted[`${doneTask.userId}`]++;
    } else {
      usersCompleted[`${doneTask.userId}`] = 1;
    }
  });
  console.log(usersCompleted);
});
