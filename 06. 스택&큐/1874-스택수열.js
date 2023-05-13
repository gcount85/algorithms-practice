const fs = require('fs');

const [n, ...originArr] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map(Number);

let sortedArr = originArr.slice().sort((a, b) => b - a);

// console.log('수열:', originArr);
// console.log('후보들:', sortedArr);

function solution() {
  let stack = new Array();
  let answer = '';

  for (const num of originArr) {
    while (stack.at(-1) !== num) {
      // console.log(stack.at(-1), num);
      if (sortedArr.length === 0) {
        return 'NO';
      }
      stack.push(sortedArr.pop());
      answer += '+ ';
    }
    if (stack.length === 0) {
      return 'NO';
    }
    stack.pop();
    answer += '- ';
  }

  return answer;
}

console.log(solution());
