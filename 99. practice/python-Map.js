let myMap = new Map();

// Using a number as a key
myMap.set(42, 'value1');
console.log(myMap.get(42)); // Output: value1

// Using a boolean as a key
myMap.set(true, 'value2');
console.log(myMap.get(true)); // Output: value2

// Using an object as a key
let anotherObject = { someProperty: 'someValue' };
myMap.set(anotherObject, 'value3');
console.log(myMap.get(anotherObject)); // Output: value3

// array를 object로 사용하면 원하는 결과 X
