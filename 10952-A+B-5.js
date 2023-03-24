const fs = require('fs');

function solution() {
  const arr = fs
    .readFileSync('./dev/stdin')
    .toString()
    .trim()
    .split('\n')
    .map((line) => line.split(' ').map((n) => Number(n)));

  //   console.log(arr);

  arr
    .slice(0, -1)
    .map((i) => i.reduce((accu, curVal) => console.log(accu + curVal)));
}

solution();
