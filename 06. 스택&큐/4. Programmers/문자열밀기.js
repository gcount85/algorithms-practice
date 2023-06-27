/* 
문자열 A의 마지막 문자를 앞으로 이동시켜 B가 되면 최소 횟수 리턴, 아니면 -1 리턴

*/

// 큐 구조 이용
function solution(A, B) {
  let answer = 0;
  if (A === B) {
    return answer;
  }

  let arrA = A.split('');
  for (let i = 0; i < A.length - 1; i++) {
    arrA.unshift(arrA.pop());
    if (arrA.join('') === B) {
      return i + 1;
    }
  }
  return -1;
}

// 문자열 두개를 연속적으로 붙여서 원형 구조처럼 만든다고 생각하고, 인덱스를 찾는 방법
function solution(A, B) {
  return (B + B).indexOf(A);
}
