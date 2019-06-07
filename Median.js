let values = [2, 56, 3, 41, 0, 4, 100, 23];

values.sort(function(a,b) {
 return a - b;
});


let lowMiddle = Math.floor( (values.length - 1) / 2);
let highMiddle = Math.ceil( (values.length - 1) / 2);
let median = ( values[lowMiddle] + values[highMiddle]) / 2;

console.log(median);