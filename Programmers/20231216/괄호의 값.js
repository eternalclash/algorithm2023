// ()  2
// []  3
// (x) 2 * x
// [x] 3 * x

function solution (x) {
   let stack = []
   answer = 0
   let temp = 1

   for(let i = 0 ; i < x.length ; i++) {
    if (x[i] == "(") {
        stack.push("(")
        temp *= 2
    }
    else if (x[i] == "[") {
        stack.push("[")
        temp *= 3
    }
    else if (x[i] == ")") {
        if (stack.length == 0 || stack[stack.length-1] == "["){
            answer = 0
            break
        }
        if (x[i-1] == "(") {
            answer += temp
        }
        stack.pop()
        temp = Math.floor(temp/2)
    }
    else{
        if (stack.length == 0 || stack[stack.length-1] == "("){
            answer = 0
            break
        }
        if (x[i-1] == "[") {
            answer += temp
        }
        stack.pop()
        temp = Math.floor(temp/3)
    }
   }
   console.log(stack.length > 0 ? 0 : answer)
} 

solution("(()[[]()])")