const { Doc } = require('yjs'); // Y.js 라이브러리에서 Doc 클래스를 가져옵니다.

const doc1 = new Doc(); // 문서 1을 생성합니다.
const doc2 = new Doc(); // 문서 2를 생성합니다.

const text1 = doc1.getText('sharedText'); // 문서 1의 공유 텍스트를 가져옵니다.
const text2 = doc2.getText('sharedText'); // 문서 2의 공유 텍스트를 가져옵니다.

text1.insert(0, '안녕하세요, '); // 문서 1에 문자열을 삽입합니다.
text2.insert(0, 'Y.js 프레임워크!'); // 문서 2에 문자열을 삽입합니다.

// 변경사항을 전파하는 예제를 위해 사용자 정의 함수를 작성합니다.
function syncDocs(docSource, docTarget) {
  const update = docSource.getText('sharedText').toDelta();
  console.log(update);
  docTarget.getText('sharedText').applyDelta(update);
}

// 문서 1의 변경사항을 문서 2에 전파합니다.
syncDocs(doc1, doc2);
syncDocs(doc2, doc1);
console.log(text1.toString()); // 출력: "안녕하세요, Y.js 프레임워크!"
console.log(text2.toString()); // 출력: "안녕하세요, Y.js 프레임워크!"
