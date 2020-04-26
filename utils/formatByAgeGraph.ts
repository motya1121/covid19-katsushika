type DataType = {
  age: string
  number: number
}

export type GraphDataType = {
  label: string
  transition: number
  cumulative: number
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType[]) => {
  const graphData: GraphDataType[] = []
  let patSum = 0
  data.forEach(d => {
    patSum += d.number
    graphData.push({
      label: d.age,
      transition: d.number,
      cumulative: patSum
    })
  })
  return graphData
}
