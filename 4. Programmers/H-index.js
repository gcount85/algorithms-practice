// 컨트롤 + 알트 + N 눌러서 실행!

function solution(citations) {
  citations.sort((a, b) => b - a);
  // console.log(citations); // 	[ 6, 5, 3, 1, 0 ]
  let temp = 0;

  for (let i = 0; i < citations.length; i++) {
    if (i + 1 >= citations[i] && citations[i + 1] <= citations[i]) {
      return citations[i];
    }
  }
}

// 내림차순 정렬
// 배열[i]보다 큰 원소가 배열[i]개 이상? 랑 같거나 큰지 확인
// 계속 업데이트

citations = [3, 0, 6, 1, 5];
solution(citations);
