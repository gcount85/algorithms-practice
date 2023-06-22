// 순열로 numbers의 조합을 다 찾아낸 다음에
// 소수 검사하여 카운팅

function getAllPermutations(array) {
  const result = [];

  // 재귀 함수
  function permute(arr, m = []) {
    // 배열의 길이가 0이 아니고, 0으로 시작하지 않는 결과만 추가
    if (m.length !== 0 && m[0] !== '0') {
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

// 소수인지 검사
function isPrime(p) {
  if (Number(p) > 1) {
    for (let i = 2; i <= Math.sqrt(Number(p)); i++) {
      if (p % i === 0) {
        return false;
      }
    }
    return true;
  }
}

function solution(numbers) {
  let answer = 0;
  const allNumbers = new Set(
    getAllPermutations(numbers.split('')).map((p) => p.join(''))
  );
  for (let p of allNumbers) {
    if (isPrime(p)) {
      answer++;
    }
  }

  return answer;
}
