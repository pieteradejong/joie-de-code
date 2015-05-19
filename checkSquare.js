function checkSquare(arrayOfPoints) {
  if (!Array.isArray(arrayOfPoints)) {
    return null;
  }
  if (arrayOfPoints.length != 4) {
    throw new Error("Must pass four points");
  }
  // data validation
  var point, toPoint, lineLength, arrayOfLineLengths = [];
  for (var i = 0; i < arrayOfPoints.length; i++) {
    point = arrayOfPoints[i];
    if (point.length != 2) {
      throw new Error("Each point must have precisely two coordinates.");
    }
    for (var j = i + 1; j < arrayOfPoints.length; j++) {
      toPoint = arrayOfPoints[j];
      lineLength = Math.sqrt(Math.pow(point[0] - toPoint[0], 2) + Math.pow(point[1] - toPoint[1], 2));
      arrayOfLineLengths.push(lineLength);  
    }
  }

  arrayOfLineLengths.sort(function(a,b) { 
    return a - b; // asc
  });
  // console.log(arrayOfLineLengths);
  // iff square, then last 2 els in array will be diags so largest; 
  // and pairs 1,2 ; 3,4 ; 5,6 will each be equal length
  var isSquare;
  if (   arrayOfLineLengths[0] == arrayOfLineLengths[1] 
      && arrayOfLineLengths[2] == arrayOfLineLengths[3]
      && arrayOfLineLengths[4] == arrayOfLineLengths[5])
  {
    isSquare = true;
  }
  else {
    isSquare = false;
  }

  return isSquare;
}

var test1 = [[0,0], [1,0], [0,1], [1,1]];
var test2 = [[1,3], [3,3], [2,4], [9,19]];
var test3 = [[4,4], [4,9], [9,9], [9,4]];
var test4 = [[0,0], [1,0], [1,1]]; // error case
var test5 = [[0,0], [1,0], [0,1], [1]]; // error case
var test6 = [[-4,-4], [-4,-9], [-9,-9], [-9,-4]];
var test7 = [[0,0], [7,5], [1,5], [6,0]];

console.log("Expect true: ", checkSquare(test1));
console.log("Expect false: ", checkSquare(test2));
console.log("Expect true: ", checkSquare(test3));
// console.log("Expect error: ", checkSquare(test4));
// console.log("Expect error: ", checkSquare(test5));
console.log("Expect true: ", checkSquare(test6));
console.log("Expect false: ", checkSquare(test7));