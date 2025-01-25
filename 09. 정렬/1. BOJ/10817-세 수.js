// https://www.acmicpc.net/problem/2752

const fs = require("fs");

const inputs = fs
  .readFileSync("./dev/stdin", "utf-8")
  .trim()
  .split(" ")
  .map(Number);
  
inputs.sort((a, b)=> a - b)
console.log(inputs[1])

  

