function reverseString(str){
   return str.split("").reduce((revString, char)=> char + revString, "");  
}
alert(reverseString("Learning JavaScript"));