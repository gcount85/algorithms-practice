const fs = require('fs');

function solution() {
  const arr = fs
    .readFileSync('./dev/stdin', 'utf-8')
    .trim()
    .split('\n')
    .map((nums) => nums.split(' ').map(Number));

  console.log(Math.min(...arr[1]), Math.max(...arr[1]));

  // 아래 방법이 훨씬 시간이 오래 걸린다
  //   let maxNum = -1000000;
  //   let minNum = Infinity;

  //   arr[1].forEach((value) => {
  //     if (value > maxNum) {
  //       maxNum = value;
  //     }
  //     if (value < minNum) {
  //       minNum = value;
  //     }
  //   });

  //   console.log(minNum, maxNum);
}

solution();
