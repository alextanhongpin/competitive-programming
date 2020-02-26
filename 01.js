// This knapsack solution does not print the
// items and the individual weights, but that
// is required to solve this question.
function knapSack (maxWeight, weights, values, n) {
  if (n === 0 || maxWeight === 0) {
    return 0
  }
  if (weights[n - 1] > maxWeight) {
    return knapSack(maxWeight, weights, values, n - 1)
  }
  return Math.max(
    values[n - 1] +
      knapSack(maxWeight - weights[n - 1], weights, values, n - 1),
    knapSack(maxWeight, weights, values, n - 1)
  )
}

function studySmart (file) {
  const [first, ...rest] = file.split('\n')
  const [numberOfTopics, hoursRemaining] = first.split(' ').map(Number)
  const topics = rest
    .slice(0, numberOfTopics)
    .map(i => i.split(' ').map(Number))
  const weights = topics.map(([, numberOfHours]) => numberOfHours)
  const values = topics.map(([marks]) => marks)
  return knapSack(hoursRemaining, weights, values, values.length)
}

const file = `5 30
10 4
16 5
22 10
29 17
23 13`

const bestScore = studySmart(file)
console.log(bestScore)
