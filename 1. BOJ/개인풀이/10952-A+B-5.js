const fs = require('fs');

function solution() {
  const arr = fs
    .readFileSync('./dev/stdin', 'utf-8') // utf-8을 인자로 추가하면 toString()을 호출할 필요X
    .trim()
    .split('\n')
    .map((line) => line.split(' ').map(Number)); // Number 메소드 바로 적용

  //   console.log(arr);

  arr.slice(0, -1).forEach((pair) => console.log(pair[0] + pair[1])); // 새로운 배열을 반환할 필요 없으므로 forEach로 충분
}

solution();
