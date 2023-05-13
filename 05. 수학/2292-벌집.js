const fs = require('fs');

let N = Number(fs.readFileSync('./dev/stdin', 'utf-8').trim());

let i = 1;
while (N >= 2) {
  N -= 6 * i;
  i++;
}
console.log(i);

// 공차가 6인 등차수열
