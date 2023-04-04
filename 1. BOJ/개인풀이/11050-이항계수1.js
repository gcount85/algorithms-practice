const fs = require('fs');

let [N, K] = fs
  .readFileSync('./dev/stdin', 'utf-8')
  .trim()
  .split(' ')
  .map(Number);

// DP (파스칼의 삼각형!)
function binomialCoefficient(n, k) {
  const dp = new Array(n + 1).fill(0).map(() => new Array(n + 1).fill(0));
  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= Math.min(i, k); j++) {
      // k보다 큰 수는 구할 필요 X
      if (j === 0 || j === i) {
        dp[i][j] = 1;
      } else {
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
      }
    }
  }
  return dp[n][k];
}

console.log(binomialCoefficient(N, K)); // 10

// 반복문
function factorial(n) {
  let count = n;
  let multiply = 1;
  while (count > 1) {
    // 무한 루프 방지
    multiply *= count;
    count--;
  }
  return multiply;
}

// 재귀
function factorial(n) {
  if (n < 2) {
    // 무한 재귀 호출 방지
    return 1;
  }
  return factorial(n - 1) * n;
}

console.log(factorial(N) / (factorial(K) * factorial(N - K)));
