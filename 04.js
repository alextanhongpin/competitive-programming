const file = `7
5 3 2 3 6 3 3`

function squareSticks (file) {
  const [first, second] = file.split('\n')
  const numberOfSticks = Number(first)
  const sticks = second.split(' ').map(Number)
  const sticksOfSameLength = sticks.reduce((counter, stick) => {
    counter[stick] = counter[stick] || 0
    counter[stick] += 1
    return counter
  }, {})
  let largestSquareArea = -Infinity
  let numberOfSquares = 0
  for (const stick in sticksOfSameLength) {
    const numberOfSticks = sticksOfSameLength[stick]
    if (numberOfSticks < 4) continue
    const squareArea = stick * stick
    if (squareArea > largestSquareArea) {
      largestSquareArea = squareArea
      numberOfSquares = Math.floor(numberOfSticks / 4)
    }
  }
  return { numberOfSquares, largestSquareArea }
}

JSON.stringify(squareSticks(file), null, 2)
