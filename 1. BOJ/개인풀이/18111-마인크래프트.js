const fs = require('fs');

const [[N, M, B], ...map] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((nums) => nums.split(' ').map(Number));

// console.log(map);

const min = Math.min(...map.flat());
const max = Math.max(...map.flat());
let count = Infinity;
let answer;

for (let i = min; i < max + 1; i++) {
  let tempBlock = B;
  let tempCount = 0;
  for (const row of map) {
    for (const height of row) {
      const gap = height - i;
      if (gap === 0) {
        continue;
      } else if (gap > 0) {
        // 땅 높이가 높아서 블록을 빼야할 때
        tempBlock += gap;
        tempCount += 2 * gap;
      } else {
        // 땅이 낮아서 블록을 쌓아야 할 때
        tempBlock += gap;
        tempCount -= gap;
      }
    }
  }
  if (tempBlock < 0) {
    continue;
  }
  if (tempCount <= count) {
    count = tempCount;
    answer = i;
  }
}

console.log(count, answer);
