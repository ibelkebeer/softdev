var fibonacci = (n) => {
  if ( n == 0 ) {
    return 0;
  }
  if ( n <= 2 ) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

var listnum = 8;
var fibnum = 0;
var list = document.getElementById("thelist");
var fibList = document.getElementById("fiblist");

list.addEventListener('mouseover', function(e) {
  console.log(e.fromElement.firstChild.nodeValue)
  document.getElementById("h").innerHTML = e.fromElement.firstChild.nodeValue;
});
list.addEventListener('mouseout', function(e) {
  document.getElementById("h").innerHTML = "Hello World!";
});
list.addEventListener('click', function(e) {
  console.log(e);
  list.removeChild(e.srcElement);
});

document.getElementById("b").addEventListener('click', function(){
    var li = document.createElement("li");
    li.innerHTML="item " + listnum;
    list.appendChild(li);
    listnum++;
});

document.getElementById("fb").addEventListener('click', function(){
    var li = document.createElement("li");
    li.innerHTML="Fib of " + fibnum + " is " + fibonacci(fibnum);
    fibList.appendChild(li);
    fibnum++;
});
