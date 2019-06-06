function largestOfFour(arr) {
  const arrayValue = 0;
  const newArray = [];
  const oldArray = arr;

  for (i = 0; i < oldArray.length; i ++) {
    for (j = 0; j < oldArray[i].length; j ++) {
      if (oldArray[i][j] > arrayValue) {
        arrayValue = oldArray[i][j];
        newArray.push(arrayValue);
      }
    }
  }
  return newArray;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);