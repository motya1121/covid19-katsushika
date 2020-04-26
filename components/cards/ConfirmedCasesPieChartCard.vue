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
      :chart-data="patientsGraph"
      :date="Data.patients.date"
      :unit="$t('人')"
    />
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
    const patientsGraph = formatByAgeGraph(Data.patients_by_age.data)

    const data = {
      Data,
      patientsGraph
    }
    return data
  }
}
</script>
