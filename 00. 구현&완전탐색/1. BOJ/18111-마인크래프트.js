// refactored
const fs = require('fs');

const [[N, M, B], ...map] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((nums) => nums.split(' ').map(Number));

const min = Math.min(...map.flat());
const max = Math.max(...map.flat());
let count = Infinity;
let answer;

for (let stdHeight = min; stdHeight < max + 1; stdHeight++) {
  let tempBlock = B;
  let tempCount = 0;
  for (const row of map) {
    for (const height of row) {
      const gap = height - stdHeight;
      if (gap === 0) {
        continue;
      }
      if (gap > 0) {
        // 땅 높이가 높아서 블록을 빼야할 때
        tempCount += 2 * gap;
      } else {
        // 땅이 낮아서 블록을 쌓아야 할 때
        tempCount -= gap;
      }
      tempBlock += gap;
    }
  }
  if (tempBlock < 0) {
    continue;
  }
  if (tempCount <= count) {
    count = tempCount;
    answer = stdHeight;
  }
}

console.log(count, answer);
