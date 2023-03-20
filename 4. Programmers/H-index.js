// 컨트롤 + 알트 + N 눌러서 실행!

function solution(citations) {
  const n = citations.length;
  citations.sort((a, b) => b - a);
  // console.log(citations); // [42, 22]
  let temp = 0;

  const minValue = Math.min(...citations);
  console.log(minValue);

  for (let i = 0; i < n; i++) {
    if (i + 1 >= citations[i]) {
      return citations[i];
    }
  }
}

// 내림차순 정렬
// 배열[i]보다 큰 원소가 배열[i]개 이상? 랑 같거나 큰지 확인
// 계속 업데이트
//           0    1
citations = [42, 22];
solution(citations);
