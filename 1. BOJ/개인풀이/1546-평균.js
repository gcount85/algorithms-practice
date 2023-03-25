const fs = require('fs');

const arr = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((nums) => nums.split(' ').map(Number));

const maxNum = Math.max(...arr[1]);

let newSum = arr[1].reduce(
  (previousValue, currentValue) =>
    previousValue + (currentValue / maxNum) * 100,
  0
); // reduce 인자로 초기값 0을 주어야 첫번째 요소도 적용 됨

console.log(newSum / arr[0]);
