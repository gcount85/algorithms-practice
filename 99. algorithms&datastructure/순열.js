// 길이가 array와 동일한 순열 리턴하기
function getPermutations(array) {
  // 결과를 저장할 빈 배열 생성
  const result = [];

  // 재귀 함수
  function permute(arr, m = []) {
    // 배열의 길이가 0일때만 추가
    if (arr.length === 0) {
      result.push(m);
    } else {
      for (let i = 0; i < arr.length; i++) {
        let curr = arr.slice();
        let next = curr.splice(i, 1);
        permute(curr.slice(), m.concat(next));
      }
    }
  }

  permute(array);

  return result;
}

console.log(getPermutations([1, 2, 3])); // 출력: [ [ 1, 2, 3 ], [ 1, 3, 2 ], [ 2, 1, 3 ], [ 2, 3, 1 ], [ 3, 1, 2 ], [ 3, 2, 1 ] ]

// 가능한 모든 길이의 순열 리턴하기
function getAllPermutations(array) {
  const result = [];

  // 재귀 함수
  function permute(arr, m = []) {
    // 배열의 길이가 0이 아닐 때만 결과에 추가
    if (m.length !== 0) {
      result.push(m);
    }
    for (let i = 0; i < arr.length; i++) {
      let curr = arr.slice();
      let next = curr.splice(i, 1);
      permute(curr.slice(), m.concat(next));
    }
  }

  permute(array);

  return result;
}

// 함수 사용 예시
console.log(getAllPermutations([1, 2, 3])); // 가능한 모든 순열
