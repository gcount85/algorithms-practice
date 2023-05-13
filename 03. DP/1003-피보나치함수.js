// https://www.acmicpc.net/problem/1003

const fs = require('fs');

const [T, ...testCases] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n');

let answer = [];

testCases.forEach((value) => {
  let memo = new Map();
  memo[0] = [1, 0];
  memo[1] = [0, 1];

  for (let i = 2; i < Number(value) + 1; i++) {
    const prev1 = memo[i - 1];
    const prev2 = memo[i - 2];

    memo[i] = [prev1[0] + prev2[0], prev1[1] + prev2[1]];
  }
  answer.push(...memo[Number(value)]);
});

console.log(...answer);

// 재귀 호출과 DP 호출의 차이를 생각해서 구현해야 함!! (재귀는 반복적으로 했던 계산을 또 한다는 점)
