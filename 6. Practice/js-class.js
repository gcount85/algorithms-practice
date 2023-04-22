class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello() {
    console.log(`내 이름은 ${this.name}이야. 그리고 ${this.age}살이야`);
  }
}

// 인스턴스 생성
person1 = new Person('홍길동', 30);
person2 = new Person('김나무', 40);

// 메소드 호출
console.log(person1.age);
console.log(person2.name);
person1.sayHello();
person2.sayHello();
