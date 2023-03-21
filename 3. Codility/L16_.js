function solution(K, A) {
  // K: 만들어야하는 로프의 최소 길이
  // A: 로프의 길이를 담은 배열

  let n = A.length;

  if (n === 1) {
    return 1;
  }

  let count = 0;
  let temp_len = 0;

  for (let i = 0; i < n; i++) {
    let s = i;
    while (s < n) {
      if (temp_len === 0 && A[s] >= K) {
        count++;
      } else if (temp_len >= K) {
        count++;
        temp_len = 0;
      } else {
        temp_len += A[s];
      }
      s++;
    }
  }

  return count;
}

console.log(solution(4, [1, 2, 3, 4, 1, 1, 3]));
