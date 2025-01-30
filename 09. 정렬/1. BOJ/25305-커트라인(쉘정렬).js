// https://www.acmicpc.net/problem/25305

const fs = require('fs');

const [[N, k], [...x]] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .split('\n')
  .map((el) => el.split(' '))
  .map((el) => el.map(Number));

// console.log(N, k, x);
// x = [100 76 85 93 98]
for (let d = Math.floor(N / 2); d >= 1; d = Math.floor(d / 2)) {
  // console.log(d); // d = 2, 1
  for (let i = d; i < N; i++) {
    // console.log(i); // i = 2, 3, 4
    let val = x[i]; // 85
    let j;
    for (j = i; j >= d && x[j - d] > val; j = j - d) {
      x[j] = x[j - d];
      // console.log(x);
    }
    x[j] = val;
  }
  console.log(x);
}

// console.log(x[N - k]);
