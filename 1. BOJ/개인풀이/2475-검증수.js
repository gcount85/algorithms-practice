const fs = require('fs');

const identiNum = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split(' ')
  .map(Number);

let identiPower = identiNum.reduce(
  (previousValue, currentValue) => previousValue + currentValue ** 2,
  0
);

console.log(identiPower % 10);
