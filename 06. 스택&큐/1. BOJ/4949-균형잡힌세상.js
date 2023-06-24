const fs = require('fs');

const N = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((value) => value.trim())
  .slice(0, -1);

let answer = [];

for (const line of N) {
  let stack = [];
  let isBalanced = 'yes';
  for (const char of line) {
    if (['[', '('].includes(char)) {
      stack.push(char);
    } else if (char === ']') {
      if (stack.at(-1) === '[') {
        stack.pop();
      } else {
        // 바로 확인 후 no 처리: 안 하면 에러(yes가 나오는 예외 케이스)
        isBalanced = 'no';
        break;
      }
    } else if (char === ')') {
      if (stack.at(-1) === '(') {
        stack.pop();
      } else {
        // 바로 확인 후 no 처리: 안 하면 에러(yes가 나오는 예외 케이스)
        isBalanced = 'no';
        break;
      }
    }
  }
  if (stack.length !== 0) {
    isBalanced = 'no';
  }
  answer.push(isBalanced);
}
console.log(...answer);
