/* 
노란 타일 개수와 갈색 타일 개수의 패턴 -> 경우의 수 완탐
1) w * h = brown + yellow
2) w + h = brown / 2 + 2

1), 2) 공식으로 완탐

 */
function solution(brown, yellow) {
  let answer = [];
  const sum = brown / 2 + 2;
  const multi = brown + yellow;
  for (let h = 3; h <= sum / 2; h++) {
    let w = multi / h;
    if (w % 1 === 0 && w + h === sum) {
      answer.push(w);
      answer.push(h);
    }
  }

  return answer;
}
