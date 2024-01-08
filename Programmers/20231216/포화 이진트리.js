function solution(numbers) {
    const answer = []
    function checkBTree(b_str,start,end) {
        const mid = Math.floor((start+end)/2)
        const left_c = Math.floor((start + mid-1)/2);
        const right_c = Math.floor((mid+1+ end)/2);

        if (start == end) {
            return true;
        }

        if(b_str[mid] == '0' && ((b_str[left_c] == '1')|| (b_str[right_c] == '1'))){
            return false;
        }

        if(!checkBTree(b_str, start, mid -1)) return false;
        if(!checkBTree(b_str, mid+1, end)) return false;
        return true; 
    }
    for (let number of numbers) {
        let bi_num = number.toString(2);
        let n = bi_num.length;
        // 0101010
        let m = n.toString(2).length //이진법으로 바기
        let bi_tree = '0'.repeat(2**m-1 - n)
        bi_tree = bi_tree +'' + bi_num;
        
        if(checkBTree(bi_tree,0,bi_tree.length-1)) {
            answer.push(1);
        }
        else{
            answer.push(0);
        }


    }
    return answer
}

console.log(solution([7,42,5]))