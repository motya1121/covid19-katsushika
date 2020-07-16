<template>
  <!--
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数')"
      :title-id="'number-of-confirmed-cases'"
      :chart-id="'time-bar-chart-patients'"
      :chart-data="patientsGraph"
      :date="Data.patients.date"
      :unit="$t('人')"
    />
  </v-col>
  -->
  <v-col cols="12" md="6" class="DataCard">
    <CircleChart
      :title="$t('感染者の状況(年代別)')"
      :title-id="'confirmed-cases-by-age'"
      :chart-id="'pie-chart-patients'"
      :chart-data="cut_Data_by_time"
      :date="Data.patients.date"
      :daterange="date_range"
      :unit="$t('人')"
      @update_cut_Data="update_cut_Data"
    />
    {{ cut_Data_by_time }}
    {{ start_date }}
    {{ end_date }}
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
      return formatByAgeGraph(Data.patients_by_age.data)
    },
    date_range() {
      // 日付の最大と最小
      return [0, 10]
    }
  },
  methods: {
    update_cut_Data(startDate, endDate) {
      this.start_date = startDate
      this.end_date = endDate
    }
  }
}
</script>
