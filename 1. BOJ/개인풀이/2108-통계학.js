const fs = require('fs');

const [N, ...numbers] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map(Number);

numbers.sort((a, b) => a - b);

let avg = Math.round(numbers.reduce((a, v) => a + v, 0) / N) || 0; // -0을 반환하는 경우 대비

const median = numbers[Math.floor(N / 2)];

const range = numbers[N - 1] - numbers[0];

const count = {};
numbers.forEach((v) => {
  count[v] = (count[v] || 0) + 1;
});
const sortedCount = Object.entries(count).sort((a, b) =>
  a[1] === b[1] ? a[0] - b[0] : b[1] - a[1]
);
const mode =
  N > 1 && sortedCount[0][1] === sortedCount[1][1]
    ? sortedCount[1][0]
    : sortedCount[0][0];
// console.log(sortedCount);

console.log(avg, median, mode, range);
