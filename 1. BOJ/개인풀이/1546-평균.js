const fs = require('fs');

const [scoreLength, scores] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((nums) => nums.split(' ').map(Number));

console.log(scoreLength);
console.log(scores);

const maxScore = Math.max(...scores);

let newSum = scores.reduce(
  (previousValue, currentValue) =>
    previousValue + (currentValue / maxScore) * 100,
  0
); // reduce 인자로 초기값 0을 주어야 첫번째 요소도 적용 됨

console.log(newSum / scoreLength);
