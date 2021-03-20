<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数')"
      :title-id="'number-of-confirmed-cases'"
      :chart-id="'time-bar-chart-patients'"
      :chart-data="patientsGraph"
      :date="date"
      :unit="$t('人')"
      :by-date="true"
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
    const patientsGraph = formatGraph(Data.patients_summary.data)
    const date = Data.patients_summary.date

    return {
      patientsGraph,
      date
    }
  }
}
</script>

<style lang="scss" scoped>
.Description-Link {
  text-decoration: none;
  @include button-text('sm');
}
.Description-ExternalLink {
  margin-bottom: 10px;
}
</style>
