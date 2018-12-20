var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

var list = document.getElementById("thelist");
list.addEventListener('mouseover', function(e) {
  console.log(e.fromElement.firstChild.nodeValue)
  document.getElementById("h").innerHTML = e.fromElement.firstChild.nodeValue;
})
list.addEventListener('mouseout', function(e) {
  document.getElementById("h").innerHTML = "Hello World!";
})
list.addEventListener('click', function(e) {
  console.log(e);
})
