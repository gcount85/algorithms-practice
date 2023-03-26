const fs = require('fs');

const [N, ...coordinates] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((value) => value.split(' ').map(Number));

let answer = '';
coordinates
  .sort((a, b) => (a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]))
  .forEach((value) => {
    answer += `${value[0]} ${value[1]}\n`;
  });

// 시간 초과 버전 (console.log를 여러 번 찍음)
// coordinates
//   .sort((a, b) => (a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]))
//   .forEach((value) => {
//     console.log(...value);
//   });

console.log(answer); // console
