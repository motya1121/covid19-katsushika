<template>
  <data-view
    :title="title"
    :title-id="titleId"
    :url="url"
    :url-text="urlText"
    :date="date"
  >
    <pie-chart
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
    <template v-slot:infoPanel>
      <data-view-basic-info-panel
        :l-text="displayInfo.lText"
        :s-text="displayInfo.sText"
        :unit="displayInfo.unit"
      />
    </template>
  </data-view>
</template>

<script>
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
export default {
  components: { DataView, DataViewBasicInfoPanel },
  props: {
    title: {
      type: String,
      required: false,
      default: ''
    },
    titleId: {
      type: String,
      required: false,
      default: ''
    },
    chartId: {
      type: String,
      required: false,
      default: 'pie-chart'
    },
    chartData: {
      type: Array,
      required: false,
      default: () => []
    },
    date: {
      type: String,
      required: true
    },
    unit: {
      type: String,
      required: false,
      default: ''
    },
    info: {
      type: String,
      required: false,
      default: ''
    },
    url: {
      type: String,
      required: false,
      default: ''
    },
    urlText: {
      type: String,
      required: false,
      default: ''
    },
    descriptions: {
      type: Array,
      required: false,
      default: () => []
    }
  },
  computed: {
    displayInfo() {
      return {
        lText: this.chartData[
          this.chartData.length - 1
        ].cumulative.toLocaleString(),
        sText: '',
        unit: this.unit
      }
    },
    displayData() {
      const colorArray = [
        '#ddffe9',
        '#aaffc8',
        '#77ffa7',
        '#44ff86',
        '#11ff65',
        '#00dd4e',
        '#00aa3c',
        '#00772a',
        '#004418',
        '#001106'
      ]
      return {
        labels: this.chartData.map(d => {
          return d.label
        }),
        datasets: [
          {
            label: this.chartData.map(d => {
              return d.label
            }),
            data: this.chartData.map(d => {
              return d.transition
            }),
            backgroundColor: this.chartData.map((d, index) => {
              return colorArray[index]
            }),
            borderColor: '#ffffff',
            borderWidth: 1
          }
        ]
      }
    },
    displayOption() {
      const unit = this.unit
      const chartData = this.chartData
      return {
        tooltips: {
          showAllTooltips: true,
          displayColors: false,
          callbacks: {
            label(tooltipItem) {
              return `${chartData[tooltipItem.index].transition} ${
                tooltipItem.index === 1 ? unit : '人'
              }`
            },
            title(tooltipItem, data) {
              return data.labels[tooltipItem[0].index]
            }
          }
        },
        responsive: true,
        maintainAspectRatio: true,
        legend: {
          display: true,
          position: 'right'
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.Graph-Desc {
  margin: 10px 0;
  font-size: 12px;
  color: $gray-3;
}
.link {
  text-decoration: none;
}
</style>
