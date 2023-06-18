// 1,2,3번은 문제를 찍는 패턴이 다 다름
// 패턴을 반복시켜서 답이랑 비교할 것

function solution(answers) {
  let answer = [];
  const one = [1, 2, 3, 4, 5];
  const two = [2, 1, 2, 3, 2, 4, 2, 5];
  const thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let 채점 = { 1: 0, 2: 0, 3: 0 };

  let i = 0;
  let [j, k, l] = [i, i, i];
  while (i < answers.length) {
    if (j === one.length) {
      j = 0;
    }
    if (k === two.length) {
      k = 0;
    }
    if (l === thr.length) {
      l = 0;
    }
    if (answers[i] === one[j]) {
      채점[1] += 1;
    }
    if (answers[i] === two[k]) {
      채점[2] += 1;
    }
    if (answers[i] === thr[l]) {
      채점[3] += 1;
    }
    i++;
    j++;
    k++;
    l++;
  }

  let 뉴배열 = Object.entries(채점).sort((a, b) => b[1] - a[1]);
  let max = 뉴배열[0][1];
  answer.push(Number(뉴배열[0][0]));

  for (let i = 1; i < 뉴배열.length; i++) {
    if (뉴배열[i][1] === max) {
      answer.push(Number(뉴배열[i][0]));
    } else {
      break;
    }
  }

  return answer;
}
