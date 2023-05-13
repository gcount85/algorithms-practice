const fs = require('fs');

const input = fs.readFileSync('./dev/stdin', 'utf-8').trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const board = input.slice(1);

// 시간 복잡도 O((N-7)*(M-7)*64)
function min_changes(row, col, board) {
  let tempCount1 = 0; // 첫 칸이 W인 경우
  let tempCount2 = 0; // 첫 칸이 B인 경우

  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if ((i + j) % 2 === 0) {
        // 짝수인 칸
        if (board[i + row][j + col] != 'W') {
          tempCount1++;
        }
        if (board[i + row][j + col] != 'B') {
          tempCount2++;
        }
      } else {
        // 홀수인 칸
        if (board[i + row][j + col] != 'B') {
          tempCount1++;
        }
        if (board[i + row][j + col] != 'W') {
          tempCount2++;
        }
      }
    }
  }
  return Math.min(tempCount1, tempCount2);
}

let minCount = Infinity;

// console.log(board);

for (let row = 0; row < N - 7; row++) {
  for (let col = 0; col < M - 7; col++) {
    minCount = Math.min(min_changes(row, col, board), minCount);
  }
}

console.log(minCount);

/*
(0,0) 부터 (m-1,n-1) 까지 완전탐색
1. 0~7열까지 확인하는데, 0,0이 W인지 B인지에 따라 카운트
    1) 왼쪽 첫 칸이 W이면 행+열이 짝수인 칸이 모두 W이여야 함/홀수인 칸은 모두 B여야 함
    2) 왼쪽 첫 칸이 B이면 행+열이 짝수인 칸이 모두 B여야 함/홀수인 칸은 W여야 함 
2. 7열에 도달하면 다음 행으로 이동. 
3. count 비교 후 최솟값으로 할당
*/
