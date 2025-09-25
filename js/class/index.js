class Animal {
  // Constructor
  constructor(name, age) {
    // Property/Attribute
    this.name = name;
    this.age = age;
  }
  
  // Methods/Functions
  getName() {
    return this.name;
  }

}

const cat = new Animal("Katze", 3)
console.log(cat.getName())