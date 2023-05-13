// https://www.acmicpc.net/problem/4153
// 피타고라스 정리 이용하면 간단

const fs = require('fs');

const triangles = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .slice(0, -1);

// console.log(triangles);

let answer = triangles.map((value) => {
  const triangle = value
    .split(' ')
    .map(Number)
    .sort((a, b) => a - b);
  if (triangle[2] ** 2 === triangle[0] ** 2 + triangle[1] ** 2) {
    return 'right';
  }
  return 'wrong';
});

console.log(...answer);
