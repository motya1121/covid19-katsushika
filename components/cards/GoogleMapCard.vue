<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('テイクアウト可能なお店')"
      :title-id="'takeout_map'"
      :date="date"
    >
      <iframe
        src="https://www.google.com/maps/d/embed?mid=1ZwfVJdk3xmXTldEfvSTggKPVeecSP5Ew&hl=ja"
        width="100%"
        height="450px"
      />
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
import DataView from '@/components/DataView.vue'

export default {
  components: {
    DataView
  },
  data() {
    return {
      // TODO: GoogleMapを更新したら更新する
      date: '2020/04/29 01:19'
    }
  }
}
</script>
