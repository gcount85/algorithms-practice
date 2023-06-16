// 가로/세로 비율을 계산해서 1 이상인 아이들은 눕힌다.
// 가장 작은 지갑의 크기를 리턴하라.

function solution(sizes) {
  let answer = 0;
  let maxWidth = 0;
  let maxHeight = 0;

  for (let i of sizes) {
    let w = i[0];
    let h = i[1];
    if (i[0] / i[1] > 1) {
      w = i[1];
      h = i[0];
    }
    if (w > maxWidth) {
      maxWidth = w;
    }
    if (h > maxHeight) {
      maxHeight = h;
    }
  }

  answer = maxWidth * maxHeight;

  return answer;
}

let sizes = [
  [60, 50],
  [30, 70],
  [60, 30],
  [80, 40],
];
console.log(solution(sizes));
