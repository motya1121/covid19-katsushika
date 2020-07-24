import dayjs from 'dayjs'

const headers = [
  { text: '公表日', value: '公表日' },
  { text: '症状', value: '症状' },
  { text: '年代', value: '年代' },
  { text: '性別', value: '性別' },
  { text: '状態', value: '状態' },
  { text: '退院※', value: '退院', align: 'center' }
]

type DataType = {
  リリース日: string
  症状: string | null
  年代: string | null
  性別: '男性' | '女性' | string
  退院: '◯' | null
  状態: string | null
  [key: string]: any
}

type TableDataType = {
  公表日: string
  症状: DataType['症状']
  年代: DataType['年代']
  性別: DataType['性別'] | '不明'
  退院: DataType['退院']
  状態: DataType['状態']
}

type TableDateType = {
  headers: typeof headers
  datasets: TableDataType[]
}

/**
 * Format for DataTable component
 *
 * @param data - Raw data
 */
export default (data: DataType[]) => {
  const tableDate: TableDateType = {
    headers,
    datasets: []
  }
  data.forEach(d => {
    const TableRow: TableDataType = {
      公表日: dayjs(d['リリース日']).format('MM/DD') ?? '不明',
      症状: d['症状'] ?? '調査中',
      年代: d['年代'] ?? '不明',
      性別: d['性別'] ?? '不明',
      退院: d['退院'],
      状態: d['状態']
    }
    tableDate.datasets.push(TableRow)
  })
  tableDate.datasets.sort((a, b) =>
    a.公表日 === b.公表日 ? 0 : a.公表日 < b.公表日 ? 1 : -1
  )
  return tableDate
}
