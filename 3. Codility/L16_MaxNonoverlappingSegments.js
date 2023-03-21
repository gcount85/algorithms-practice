// 100%
function solution(A, B) {
  let n = B.length;

  // 빈 배열 예외처리 하지 않으면 count 에러
  if (n === 0) {
    return 0;
  }

  let count = 1;
  let end = B[0];

  // 끝점과 다음 선분의 시작점을 비교하여 중첩 선분 개수 계산
  for (let i = 0; i < n; i++) {
    if (A[i] > end) {
      count++;
      end = B[i];
    }
  }
  return count;
}
