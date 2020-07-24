<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('感染者の状況')"
      :title-id="'details-of-confirmed-cases'"
      :date="Data.patients.date"
    >
      <confirmed-cases-details-table
        :aria-label="$t('感染者の状況')"
        v-bind="confirmedCases"
      />
      <template v-slot:footer>
        <OpenDataLink
          url="https://raw.githubusercontent.com/motya1121/covid19-katsushika/master/tool/covid_data/data/row_data.json"
        />
      </template>
    </data-view>
  </v-col>
</template>

<style lang="scss" module>
.note {
  margin-top: 10px;
  margin-bottom: 0;
  font-size: 12px;
  color: $gray-3;
}
</style>

<script>
import Data from '@/data/data.json'
import formatConfirmedCases from '@/utils/formatConfirmedCases'
import DataView from '@/components/DataView.vue'
import ConfirmedCasesDetailsTable from '@/components/ConfirmedCasesDetailsTable.vue'
import OpenDataLink from '@/components/OpenDataLink.vue'

export default {
  components: {
    DataView,
    ConfirmedCasesDetailsTable,
    OpenDataLink
  },
  data() {
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(Data.main_summary)

    const data = {
      Data,
      confirmedCases
    }
    return data
  }
}
</script>
