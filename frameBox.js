const frame = sentence => {
    const arr = sentence.split(" ")
    const longest = arr.reduce((a, b) => a.length > b.length ? a : b)
  
    console.log("#".repeat(longest.length + 4))
  
    arr.forEach(word => {
      console.log(`# ${word + " ".repeat(longest.length - word.length)} #`)
    })
  
    console.log("#".repeat(longest.length + 4))
  }
  
  frame("hello world i am paul")
  
  