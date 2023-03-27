const fs = require('fs');

const [A, B] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split(' ')
  .map(Number)
  .sort((a, b) => b - a);

// console.log(A, B);

// 최대공약수 (유클리드 호제법)
let num1 = A;
let num2 = B;
let remainder = -1;

while (remainder !== 0) {
  remainder = num1 % num2;
  num1 = num2;
  num2 = remainder;
}

console.log(num1);

// 최소공배수 (최대공약수를 이용한 방법)
const n1 = A / num1;
const n2 = B / num1;
const lcm = num1 * n1 * n2;

console.log(lcm);
