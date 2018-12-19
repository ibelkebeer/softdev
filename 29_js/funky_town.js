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

var students = ["Tim", "Tom", "Timmothy", "Tommothy", "William", "Imad"];
var randomStudent = () => {
  return students[Math.floor(Math.random() * students.length)];
}

document.getElementById("a").addEventListener("click", function() {
  var output = fibonacci(5);
  document.getElementById("fib").innerHTML = "fibonacci(5): " + output;
  console.log(output);
});
document.getElementById("b").addEventListener("click", function() {
  var output = gcd(26, 52);
  document.getElementById("gcd").innerHTML = "gcd(26,52): " + output;
  console.log(output);
});
document.getElementById("c").addEventListener("click", function() {
  var output = randomStudent();
  document.getElementById("rs").innerHTML = "randomStudent(): " + output;
  console.log(output);
});
