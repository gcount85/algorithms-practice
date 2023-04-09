// https://www.acmicpc.net/problem/2839

const fs = require('fs');

const N = Number(fs.readFileSync('./dev/stdin', 'utf-8').trim());

// console.log(N);

/* 2개로 n kg 을 맞추려면, 1개일 때 경우의 수에 +3 or +5kg을 해본다! */

// let memo = new Array(N + 1).fill(
//   new Array(Math.floor(N / 3) + 1).fill(Infinity)
// ); // 이중 배열 필요 없다

let memo = new Array(N + 1).fill(-1);
memo[3] = 1;
memo[5] = 1;
console.log(memo);
function dp(N) {
  for (let weight = 3; weight < N + 1; weight++) {
    if (weight - 3 >= 0 && memo[weight - 3] !== -1) {
      memo[weight] = memo[weight - 3] + 1;
    }
    if (weight - 5 >= 0 && memo[weight - 5] !== -1) {
      memo[weight] = memo[weight - 5] + 1;
    }
  }
  console.log(memo);
  return memo[N];
}

console.log(dp(N));
