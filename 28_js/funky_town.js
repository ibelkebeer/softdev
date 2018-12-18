var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

var gcd = (a, b) => {
  if ( b == 0 ) {
    return a;
  }
  return gcd(b, a % b);
}

var students = ["Tim", "Tom", "Timmothy", "Tommothy"];
var randomStudent = () => {
  return students[Math.floor(Math.random() * students.length)];
}
