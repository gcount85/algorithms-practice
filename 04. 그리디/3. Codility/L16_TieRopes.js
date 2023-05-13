// 25%
// function solution(K, A) {
//   // K: 만들어야하는 로프의 최소 길이
//   // A: 로프의 길이를 담은 배열

//   let n = A.length;
//   let count = 0;
//   let maxCount = 0;
//   let temp_len = 0;

//   for (let i = 0; i < n; i++) {
//     let s = i;
//     while (s < n) {
//       if (temp_len === 0 && A[s] >= K) {
//         count++;
//       } else if (temp_len >= K) {
//         count++;
//         temp_len = 0;
//       } else if (A[s] >= K) {
//         count++;
//       } else {
//         temp_len += A[s];
//       }
//       s++;
//     }
//     maxCount = Math.max(count, maxCount);
//     count = 0;
//   }
//   return maxCount;
// }

// 100%
function solution(K, A) {
  // K: 만들어야하는 로프의 최소 길이
  // A: 로프의 길이를 담은 배열

  let count = 0;
  let temp_len = 0;
  let n = A.length;

  for (let i = 0; i < n; i++) {
    temp_len += A[i];
    if (temp_len >= K) {
      count++;
      temp_len = 0;
    }
  }

  return count;
}

K = 4;
A = [1, 2, 3, 4, 1, 1, 3];
A = [1];
console.log(solution(K, A));
