const fs = require('fs');

// refactored : O(N * log(log(N)))
function solution() {
  const [M, N] = fs
    .readFileSync('./dev/stdin', 'utf-8')
    .trim()
    .split(' ')
    .map(Number);

  // true = 소수임 or 방문한 적 없음, false = 소수 아님
  let prime = new Array(N + 1).fill(true);
  prime[0] = prime[1] = false;

  for (let num = 2; num * num < N + 1; num++) {
    if (prime[num]) {
      // for (let i = 2; i < num; i++) { // 이 부분 무의미. 배수 지우기 작업만 하면 충분
      //   if (num % i === 0) {
      //     prime[num] = false;
      //     break;
      //   }
      // }
      for (let j = num ** 2; j < N + 1; j += num) {
        prime[j] = false;
      }
    }
  }

  let answer = [];
  for (let k = M; k < N + 1; k++) {
    if (prime[k]) {
      answer.push(k);
    }
  }
  process.stdout.write(answer.join('\n')); // console.log를 일일이 찍는 것보다 이렇게 하는 것이 훨씬 효율적
  // console.log(...answer);
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
