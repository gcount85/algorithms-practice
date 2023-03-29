const fs = require('fs');

const [[K, N], ...lines] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split('\n')
  .map((nums) => nums.split(' ').map(Number));

const sortedLines = lines.flat().sort((a, b) => a - b);
// console.log(sortedLines);

let l = 0;
let h = Math.max(...sortedLines);
let m = 0;
let answer = [];

while (l <= h) {
  m = Math.floor((l + h) / 2);
  const cutLines = sortedLines.reduce(
    (previousValue, currentValue) =>
      previousValue + Math.floor(currentValue / m),
    0
  );

  if (cutLines >= N) {
    l = m + 1;
    answer.push(m);
  } else {
    h = m - 1;
  }
}
console.log(Math.max(...answer));

/*
- 조건
    - 같은 길이의 N개의 랜선이 필요함 
    - 각기 다른 길이의 K개의 랜선을 자를 것임
    - 이미 자른 랜선은 붙일 수 없음
    - 기존 K개로 N개의 랜선을 만들 수는 없음 
    - *N개보다 많이 만들어도 됨* 
    - K <= N
- 리턴
    - 만들 수 있는 최대 랜선의 길이 
    
- 의사코드
    - (나무 자르기 같은 문제)
    1) K개의 랜선 길이별로 정렬
    2) 랜선 리스트를 이분탐색
        1_ m의 길이로 잘랐을 때 생성되는 랜선 개수가 N개 이상이면: 길이를 더 높게
        2_ 아니라면: 길이를 더 낮게
  
  */
