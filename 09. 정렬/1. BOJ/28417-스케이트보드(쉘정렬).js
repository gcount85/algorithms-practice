// https://www.acmicpc.net/problem/28417

const fs = require('fs');

const [[N], ...score] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .split('\n')
  .map((el) => el.split(' '))
  .map((el) => el.map(Number));

// 0 1 2 3 4
// 5 4 3 2j 1i
const shellSort = (len, array) => {
  for (let d = Math.floor(len / 2); d >= 1; d = Math.floor(d / 2)) {
    // d = 2, 1
    for (let i = d; i < array.length; i++) {
      // i = 1, 2, 3, 4
      let temp = array[i]; // temp 값을 최종 j의 위치에 넣는 것이 핵심.

      /** 틀린 쉘 정렬 코드 */
      // if (array[i] > array[i - d]) {
      //   array[i] = array[i - d];
      //   array[i - d] = temp;
      // }

      let j = i;
      while (j >= d && array[j - d] < temp) {
        array[j] = array[j - d];
        j -= d;
      }
      array[j] = temp;
    }
    // console.log(array);
  }
  return array;
};

let winner = 0;
score.forEach((v) => {
  const sorted = shellSort(v.length - 2, v.slice(2));
  let finalScore = Math.max(v[0], v[1]) + sorted[0] + sorted[1];
  winner = finalScore > winner ? finalScore : winner;
});
console.log(winner);
