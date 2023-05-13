// https://www.acmicpc.net/problem/2920
// 자바스크립트 입력은 ./dev/stdin에서!

const fs = require('fs');

function solution() {
  const pitch = fs
    .readFileSync('./dev/stdin', 'utf-8')
    .trim()
    .split(' ')
    .map(Number);

  console.log(pitch);

  const n = pitch.length;
  let flag = 'ascending';
  let gap = -1;
  if (pitch[0] === '8') {
    flag = 'descending';
    gap = 1;
  }

  for (let i = 0; i < n - 1; i++) {
    if (pitch[i] - pitch[i + 1] != gap) {
      return 'mixed';
    }
  }
  return flag;
}

// refactored
function solution() {
  const pitch = fs
    .readFileSync('./dev/stdin', 'utf-8')
    .trim()
    .split(' ')
    .map(Number);

  // console.log(pitch);

  const isAscending = pitch
    .slice(1)
    .every((value, index) => value === pitch[index] + 1);
  const isDescending = pitch
    .slice(1)
    .every((value, index) => value === pitch[index] - 1);

  return isAscending ? 'ascending' : isDescending ? 'descending' : 'mixed';
}

console.log(solution());
