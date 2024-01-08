class Heap {
  constructor() {
    this.heap = [null];
  }
  heappush(value) {
    this.heap.push(value)
    let currentIndex = this.heap.length - 1
    let parentIndex = (currentIndex / 2) >> 0;

    while(currentIndex > 1 && this.heap[parentIndex] > this.heap[currentIndex]) {
        [this.heap[parentIndex], this.heap[currentIndex]] = [this.heap[currentIndex],this.heap[parentIndex]]
        currentIndex = parentIndex
        parentIndex = (currentIndex/2) >> 0
    }
  }
  
  heappop() {
    // [null,2,4,3]
    //1.제일 작은 값을 뺴고
    // 2.부모 노드 위치에 그 다음 작은 값을 넣어줘야 되는거야
    const min = this.heap[1] // 배열의 첫번째 힙의 제일 높은 순위
    if( this.heap.length<=2 ) this.heap = [null] //부모와 자식노드 둘 다 존재하지 않기에 2번 목적할 필요없다
    else this.heap[1] = this.heap.pop();
    let parentIndex = 1
    let leftChildIndex = parentIndex * 2
    let rightChildIndex =parentIndex * 2 + 1
    // 왼오른 둘 다 없을 떄, 왼만 있을 때, 왼 오른 둘 다 있을 때
    if (!this.heap[leftChildIndex]) return min;
    if (!this.heap[rightChildIndex]) {
        if(this.heap[leftChildIndex] < this.heap[parentIndex]) {
            [this.heap[leftChildIndex],this.heap[parentIndex]] =[this.heap[parentIndex],this.heap[leftChildIndex]]     
        }
        return min;
    }
    while (this.heap[leftChildIndex] < this.heap[parentIndex] || this.heap[rightChildIndex] < this.heap[parentIndex]) {
        const minIndex = this.heap[leftChildIndex] > this.heap[rightChildIndex] ? rightChildIndex : leftChildIndex;
        [this.heap[minIndex], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[minIndex]]
        parentIndex = minIndex
        leftChildIndex = parentIndex * 2
        rightChildIndex = parentIndex * 2 + 1
    }
    return min
  }
}
const heap = new Heap()
heap.heappush(3)
console.log(heap.heap)
heap.heappush(5)
heap.heappush(4)
console.log(heap.heap)
heap.heappush(1)
console.log(heap.heap)
console.log(heap.heappop())
console.log(heap.heap)
// 2
 
// 1 3 
// 4 5 6  7

// 부모노드

// 2 1 3 -> 왼쪽 녀석만 낮을 때
// 2 3 1 -> 오른쪽 녀석만 낮을 때
// 3 1 2 -> 자식 둘 다 부모보다 낮을 떄
// 1 3 2

// 부모노드의 인덱스 * 2 왼쪽 자식노드
// 부모노드의 인덱스 * 2 + 1 오른쪽 자식노드

//    1
//   2 3
//  3 2 


// 1~3 , 4~6, 2~4