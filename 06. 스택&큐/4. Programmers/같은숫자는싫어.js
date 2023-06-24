// 평범한 스택 사용 -> 효율성 테스트 실패
function solution1(arr) {
  let answer = [];
  while (arr.length !== 0) {
    let shifted = arr.shift();
    if (shifted === answer.at(-1)) {
      answer.pop();
    }
    answer.push(shifted);
  }

  return answer;
}

// arr 반복 방식 -> 100점
function solution2(arr) {
  let answer = [];
  let comp = undefined;
  for (let i of arr) {
    if (i !== comp) {
      answer.push(i);
    }
    comp = i;
  }

  return answer;
}
