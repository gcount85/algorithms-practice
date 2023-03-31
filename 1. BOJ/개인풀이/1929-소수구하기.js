const fs = require('fs');

// 시간초과
function solution() {
  const [M, N] = fs
    .readFileSync('./dev/stdin', 'utf-8')
    .trim()
    .split(' ')
    .map(Number);

  // true = 소수임 or 방문한 적 없음, false = 소수 아님
  let prime = new Array(N + 1).fill(true);
  prime[0] = prime[1] = false;

  for (let num = M; num < N + 1; num++) {
    if (prime[num] === true) {
      for (let i = 2; i < num; i++) {
        if (num % i === 0) {
          prime[num] = false;
          break;
        }
      }
      for (let j = num * 2; j < Math.sqrt(N + 1) + 1; j *= 2) {
        if (prime[j] === true) {
          prime[j] = false;
        }
      }
      if (prime[num] === true) {
        console.log(num);
      }
    }
  }
}

solution();

/*  
1. 1부터 1000000까지 소수를 모두 구한다 (에라토스테네스의 prime)
    1) 1부터 백만까지의 배열 생성
    2) TRUE인지 확인(소수이거나 방문하지 않은 인덱스)
    3) 소수인지 확인
    4) 그 숫자의 배수를 모두 소수에서 제외함(FALSE로 바꿈)
2. M이상, N 이하의 소수들 리턴
*/
