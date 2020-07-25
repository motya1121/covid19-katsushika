<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数')"
      :title-id="'number-of-confirmed-cases'"
      :chart-id="'time-bar-chart-patients'"
      :chart-data="cut_Data_by_time"
      :date="Data.patients.date"
      :daterange="date_range"
      :min-date-number="min_date_number"
      :max-date-number="max_date_number"
      :start-date-string="start_date_string"
      :end-date-string="end_date_string"
      :unit="$t('人')"
      @update_cut_Data="update_cut_Data"
    >
      <template v-slot:description>
        <ul class="ListStyleNone">
          <li>
            {{ $t('（注）患者数は選択期間内') }}
          </li>
          <li>
            {{ $t('（注）累計のグラフは選択期間内') }}
          </li>
        </ul>
      </template>
    </time-bar-chart>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatGraph from '@/utils/formatGraph'
import TimeBarChart from '@/components/TimeBarChart.vue'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 感染者数グラフ
    const data = {
      Data,
      start_date_number: 0,
      end_date_number: 0
    }
    return data
  },
  computed: {
    cut_Data_by_time() {
      const PatientsSummary = Data.patients_summary.data
      const ExportData = []
      for (const i in PatientsSummary) {
        if (this.start_date_number <= i && i <= this.end_date_number) {
          ExportData.push(PatientsSummary[i])
        }
      }
      return formatGraph(ExportData)
    },
    startDT() {
      return new Date(Data.patients_summary.data[0]['日付'])
    },
    endDT() {
      return new Date(Data.patients_summary.data.slice(-1)[0]['日付'])
    },
    min_date_number() {
      return 0
    },
    max_date_number() {
      const diff = this.endDT.getTime() - this.startDT.getTime()
      const CountDateNumber = diff / (1000 * 60 * 60 * 24)
      return CountDateNumber
    },
    date_range() {
      // 現在選択されている日付の最大最小
      return [this.start_date_number, this.end_date_number]
    },
    start_dt() {
      const tempDt = new Date(Data.patients_summary.data[0]['日付'])
      tempDt.setDate(this.startDT.getDate() + this.start_date_number)
      return tempDt
    },
    start_date_string() {
      return (
        String(this.start_dt.getMonth() + 1) +
        '/' +
        String(this.start_dt.getDate())
      )
    },
    end_dt() {
      const tempDt = new Date(Data.patients_summary.data[0]['日付'])
      tempDt.setDate(this.startDT.getDate() + this.end_date_number)
      return tempDt
    },
    end_date_string() {
      return (
        String(this.end_dt.getMonth() + 1) + '/' + String(this.end_dt.getDate())
      )
    }
  },
  created() {
    this.end_date_number = this.max_date_number
  },
  methods: {
    update_cut_Data(startDateNumber, endDateNumber) {
      this.start_date_number = startDateNumber
      this.end_date_number = endDateNumber
    }
  }
}
</script>
