<template>
  <v-col cols="12" md="6" class="DataCard">
    <CircleChart
      :title="$t('感染者の状況(年代別)')"
      :title-id="'confirmed-cases-by-age'"
      :chart-id="'pie-chart-patients'"
      :chart-data="cut_Data_by_time"
      :date="Data.patients.date"
      :daterange="date_range"
      :start-date="start_date"
      :end-date="end_date"
      :start-date-string="start_date_string"
      :end-date-string="end_date_string"
      :unit="$t('人')"
      @update_cut_Data="update_cut_Data"
    />
    {{ cut_Data_by_time }}
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import formatByAgeGraph from '@/utils/formatByAgeGraph'
import CircleChart from '@/components/CircleChart.vue'

export default {
  components: {
    CircleChart
  },
  data() {
    // 感染者数グラフ

    return {
      Data,
      start_date: 0,
      end_date: 0
    }
  },
  computed: {
    cut_Data_by_time() {
      // start_dateとend_dateの間のデータを切り出す
      const InitData = [
        {
          age: '10歳未満',
          number: 0
        },
        {
          age: '10代',
          number: 0
        },
        {
          age: '20代',
          number: 0
        },
        {
          age: '30代',
          number: 0
        },
        {
          age: '40代',
          number: 0
        },
        {
          age: '50代',
          number: 0
        },
        {
          age: '60代',
          number: 0
        },
        {
          age: '70代',
          number: 0
        },
        {
          age: '80代',
          number: 0
        }
      ]
      for (const patient of Data.patients.data) {
        if (
          this.start_dt <= new Date(patient.date) &&
          new Date(patient.date) <= this.end_dt
        ) {
          for (const AgeCount of InitData) {
            if (AgeCount.age === patient['年代']) {
              AgeCount.number++
            }
          }
        }
      }
      return formatByAgeGraph(InitData)
    },
    startDT() {
      return new Date(Data.patients_summary.data[0]['日付'])
    },
    endDT() {
      return new Date(Data.patients_summary.data.slice(-1)[0]['日付'])
    },
    date_range() {
      // 日付の最大と最小
      const diff = this.endDT.getTime() - this.startDT.getTime()
      const CountDateNumber = diff / (1000 * 60 * 60 * 24)
      return [0, CountDateNumber]
    },
    start_dt() {
      const tempDt = new Date(Data.patients_summary.data[0]['日付'])
      tempDt.setDate(this.startDT.getDate() + this.start_date)
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
      tempDt.setDate(this.startDT.getDate() + this.end_date)
      return tempDt
    },
    end_date_string() {
      return (
        String(this.end_dt.getMonth() + 1) + '/' + String(this.end_dt.getDate())
      )
    }
  },
  mounted() {
    this.start_date = this.date_range[0]
    this.end_date = this.date_range[1]
  },
  methods: {
    update_cut_Data(startDate, endDate) {
      this.start_date = startDate
      this.end_date = endDate
    }
  }
}
</script>
