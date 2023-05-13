const fs = require('fs');

const input = fs.readFileSync('./dev/stdin', 'utf-8').trim().split('');
const alphabet = 'abcdefghijklmnopqrstuvwxyz';

let position = alphabet.split('').map(
  (value) => input.findIndex((v) => v == value) // arr에서 알파벳의 밸류 위치 찾기
);
console.log(...position);
