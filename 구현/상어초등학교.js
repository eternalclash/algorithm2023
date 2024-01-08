const fs = require("fs");
const input = fs.readFileSync("예제.txt").toString().trim().split(`\n`);
let [N, ...arr] = input;
arr = arr.map((a) => a.split(" ").map((e) => +e));
const obj = {};
const table = Array.from({ length: N }, () =>
  Array.from({ length: N }, () => 0)
);

function checkPoint(arr, x, y) {
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  for (let direction of directions) {
    let dx = x + direction[0];
    let dy = y + direction[1];
    if (
      0 <= dx &&
      dx < arr.length &&
      0 <= dy &&
      dy < arr[0].length &&
      arr[dx][dy] != -1
    ) {
      arr[dx][dy] += 1;
    }
  }
  return arr;
}

function directNumber(arr, x, y) {
  let num = 0;
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  for (let direction of directions) {
    let dx = x + direction[0];
    let dy = y + direction[1];
    if (
      0 <= dx &&
      dx < arr.length &&
      0 <= dy &&
      dy < arr[0].length &&
      arr[dx][dy] != -1
    ) {
      num += 1;
    }
  }
  return num;
}

function makeLocation(arr) {
  let max = 0;
  let direct = 0;
  let where = [99999,99999]
  for (let i = 0; i < arr.length; i++)
    for (let j = 0; j < arr[0].length; j++) {
      if (arr[i][j] > max && arr[i][j] != -1) {
        where = [i, j];
        max = arr[i][j];
        direct = directNumber(arr, i, j);
      }
      if (arr[i][j] == max && arr[i][j] != -1) {
        let k = directNumber(arr, i, j);
        if (k == direct && (i < where[0] || (i == where[0] && j < where[1]))) {
          where = [i, j];
          direct = k;
          continue;
        }
        if (k > direct) {
          where = [i, j];
          direct = k;
        }
      }
    }
  return where;
}
for (let x of arr) {
  let temp = table.map((x, i) =>
    x.map((_, j) => {
      if (table[i][j] != 0) return -1;
      else return 0;
    })
  );
  const [start, ...friends] = x;
  obj[start] = friends;
  // 배열에 점수화를 도입
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (obj[start].find((e) => e == table[i][j])) {
        temp = checkPoint(temp, i, j);
      }
    }
  }
  const [a, b] = makeLocation(temp);
  table[a][b] = start;
}
const happy = [0,1,10,100,1000]
let answer = 0
for (let i = 0; i < table.length; i++) 
    for (let j = 0; j < table.length; j++) {
        let num =0
        for (let direction of [[0,1],[1,0],[0,-1],[-1,0]]) {
            let di = i + direction[0]
            let dj = j + direction[1]
            if (0<=di && di < table.length && 0<=dj && dj < table[0].length) {
                if (obj[table[i][j]].includes(table[di][dj])) num++
            }
        }
        answer += happy[num]
    }
console.log(answer)