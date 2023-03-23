// https://www.acmicpc.net/problem/2920
// 자바스크립트 입력은 ./dev/stdin에서!

const fs = require('fs');

function solution() {
  const 음계 = fs.readFileSync('./dev/stdin').toString().trim().split(' ');

  //   console.log(음계);

  const n = 음계.length;
  let flag = 'ascending';
  let gap = -1;
  if (음계[0] === '8') {
    flag = 'descending';
    gap = 1;
  }

  for (let i = 0; i < n - 1; i++) {
    if (음계[i] - 음계[i + 1] != gap) {
      return 'mixed';
    }
  }
  return flag;
}

console.log(solution());
