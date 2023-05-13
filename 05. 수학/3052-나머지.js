const fs = require('fs');

const arr = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map(Number);

// console.log(arr);

const divisors = arr.map((value) => value % 42);

console.log(new Set(divisors).size); // set로 중복 제거
