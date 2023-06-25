/* 
(100 - progress[i]) / speeds[i] => 얘를 올림하면 소요 기간임 
소요 기간 스택의 원소를 하나하나 pop 하면서 비교한다 
a 보다 작거나 같으면 모두 빼고 count한다. 
a 보다 큰 숫자가 나오면 count를 0으로 리셋하고 반복한다. 

*/

function solution(progresses, speeds) {
  let answer = [];
  let time = progresses.map((value, index) =>
    Math.ceil((100 - value) / speeds[index])
  );

  let top = time[0];
  let count = 0;
  for (let i of time) {
    if (i <= top) {
      count++;
    } else {
      answer.push(count);
      top = i;
      count = 1;
    }
  }
  answer.push(count);

  return answer;
}
