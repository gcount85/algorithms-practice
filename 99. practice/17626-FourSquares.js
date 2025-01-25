/**
 * https://www.acmicpc.net/problem/17626
 * 
 * 자연수를 넷 이하의 제곱수의 합으로 표현하기. 복수의 방법이 존재할 수 있음.
 * 자연수 n에 대해서 n을 최소 개수의 제곱수 합으로 표현하면?
 * 1 <= n <= 50000
 *
 * 1. n의 제곱근 이하부터 탐색
 *
 */

const fs = require("fs");

const n = Number(fs.readFileSync("./dev/stdin", "utf-8").trim());
const m = n;
const nSqrt = Math.sqrt(n);
let sum = 0;

while (sum !== n) {
  // nsqrt = n의 제곱근과 가장 가까운 자연수의 제곱
  // sum이 nsqrt의 제곱과 같으면,
  // nsqurt를 정답 배열에 push
  // m에서 sum 뺀 값이 다시 m이 된다
  // 만약 m이 0이면 break 하고, 배열 길이 반환
  // 만약 배열 원소가 4개 초과면, 배열 비우고, nsqrt에서 1을 빼서 루프 재진행
}

console.log(n);
