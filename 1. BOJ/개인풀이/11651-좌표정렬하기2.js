// https://www.acmicpc.net/problem/11651

const fs = require('fs');

const [N, ...coordinates] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((value) => value.split(' ').map(Number));

let arr = [];
coordinates
  .sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]))
  .forEach((value) => {
    arr.push(value[0], value[1]);
  });

console.log(...arr); // 입출력은 되도록 한 번만 하는 것이 시간 효율적.
