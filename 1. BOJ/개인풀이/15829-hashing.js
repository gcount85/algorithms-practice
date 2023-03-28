// 100점
const fs = require('fs');

let [L, str] = fs.readFileSync('./dev/stdin', 'utf-8').trim().split('\n');

const l = +L;
const MOD = 1234567891;
let hashValue = 0;
let pow31 = 1;

for (let i = 0; i < l; i++) {
  hashValue += (str.charCodeAt(i) - 96) * pow31; // 12줄과 13줄을 분리해야 100점!
  hashValue %= MOD;
  pow31 = (pow31 * 31) % MOD;
}

console.log(hashValue);

// 50점
// const fs = require('fs');

// let [L, str] = fs.readFileSync('./dev/stdin', 'utf-8').trim().split('\n');

// const MOD = 1234567891;
// let pow31 = 1;
// let hashValue = 0;

// for (let i = 0; i < L; i++) {
//   const charValue = str[i].charCodeAt(0) - 96;
//   hashValue = (hashValue + ((charValue * pow31) % MOD)) % MOD;
//   pow31 = pow31 * 31;
// }

// console.log(hashValue);
