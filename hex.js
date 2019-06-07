const color = () => {
  const options = "abcdef0123456789".split("")
  let answer = "#"
  for(i=0; i<6; i++) {
    answer += options[Math.floor(Math.random() * options.length)]
  }
  return answer
}