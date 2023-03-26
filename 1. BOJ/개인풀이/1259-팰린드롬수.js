const fs = require('fs');

// refactored
function isPalindrome(value) {
  let s = 0;
  let e = value.length - 1;
  while (s < e) {
    // 투 포인터로 접근
    if (value[s] !== value[e]) {
      return false;
    }
    s++;
    e--;
  }
  return true;
}

const arr = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .slice(0, -1);

const answer = arr.map((value) => (isPalindrome(value) ? 'yes' : 'no'));

console.log(...answer);

/* 기존 코드 */

// const arr = fs
//   .readFileSync('./dev/stdin', 'utf-8')
//   .trim()
//   .split('\n')
//   .slice(0, -1);

// let answer = arr.map((value) => {
//   let s = 0;
//   let e = value.length - 1;
//   while (s !== Math.floor(value.length / 2)) {
//     if (value[s] === value[e]) {
//       s++;
//       e--;
//     } else {
//       return 'no';
//     }
//   }
//   return 'yes';
// });

// console.log(...answer);
