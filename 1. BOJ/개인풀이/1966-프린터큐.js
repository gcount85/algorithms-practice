const fs = require('fs');

const [[T], ...testQueue] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((nums) => nums.split(' ').map(Number));

// console.log(testQueue);
for (let i = 0; i < T; i++) {
  const [N, M] = testQueue[i * 2];
  const queue = testQueue[i * 2 + 1];
  let queueCopy = [...queue];
  queueCopy[M] = [queueCopy[M], 't'];

  let count = 1;
  while (true) {
    let maxNum = Math.max(...queue);
    let indexOfMax = queue.indexOf(maxNum);
    let x = queueCopy.shift();
    let tag = null;

    if (typeof x === 'object') {
      tag = x[1];
      x = x[0];
    }
    if (x === maxNum) {
      if (tag) {
        console.log(count);
        break;
      }
      queue.splice(indexOfMax, 1);
      count++;
    } else {
      if (tag) {
        queueCopy.push([x, tag]);
      } else {
        queueCopy.push(x);
      }
    }
  }
}

/*
- 리턴
현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
(중요도 순으로 인쇄되게 됨)
*/
