function isPalindrome(string) {
  var answer = true, l = string.length;
  var hi = Math.floor(l/2);
  for (var i = 0; i < hi; i++)  {
    if (string[i] !== string[l - 1 - i]) {
      answer = false;
    }
  }
  return answer;
}

function sumspecial() {
  var args = Array.prototype.slice.call(arguments);
  if (args.length === 2) {
    return args[0] + args[1];
  }
  else if (args.length === 1) {
    var a = args[0];
    return function (b) {
      return a + b;
    }
  }
}


function bla() {
  var arr = [];
  for (var i = 1; i < 3; i++) {
    arr.push(function () {
      console.log(i++);
    });
  }
  arr[0]();
  arr[1]();
  arr[2]();
  arr[3]();
}

