(window.webpackJsonp=window.webpackJsonp||[]).push([[16],{493:function(t){t.exports=JSON.parse('{"date":"2020/4/9 18:00","datasets":[{"label":"2/10~14","data":[-0.96,-2.94,-7.48]},{"label":"2/17~21","data":[-0.36,-4.11,-6.95]},{"label":"2/25~28","data":[3.06,-9.47,-7.31]},{"label":"3/2~06","data":[0.47,-22.36,-10.16]},{"label":"3/9~13","data":[-1.22,-24.87,-12.05]},{"label":"3/16~19","data":[-1.36,-23.98,-11.22]},{"label":"3/23~27","data":[-4.28,-26.27,-14.34]},{"label":"3/30~03","data":[-9.93,-34.5,-30.62]},{"label":"4/6~09","data":[-21.23,-49.03,-50.03]}],"labels":["6:30~7:30","7:30~9:30","9:30~10:30"],"base_period":"1/20~1/24"}')},494:function(t){t.exports=JSON.parse('{"date":"2020/4/13 11:00","labels":["1/1~1/5","1/6~1/12","1/13~1/19","1/20~1/26","1/27~2/2","2/3~2/9","2/10~2/16","2/17~2/23","2/24~3/1","3/2~3/8","3/9~3/15","3/16~3/22","3/23~3/29","3/30~4/5","4/6~4/12"],"datasets":[{"label":"第一庁舎計","data":[0,12572,10267,12387,12248,12924,10221,12690,8841,9468,8930,7807,10368,8686,3227]},{"label":"第二庁舎計","data":[0,14656,11548,13963,13611,13711,10997,14374,10734,12271,12045,10741,13442,9343,3879]},{"label":"議事堂計","data":[0,422,316,321,632,492,464,553,492,381,540,429,444,296,87]}]}')},508:function(t,e,r){"use strict";r.r(e);var o=r(104),n=r(493),c=r(494),d=r(353),l=r(351),m=r(352),h={components:{ConfirmedCasesDetailsCard:d.a,ConfirmedCasesNumberCard:l.a,ConfirmedCasesAttributesCard:m.a},data:function(){var title,t;switch(this.$route.params.card){case"details-of-confirmed-cases":title=this.$t("検査陽性者の状況"),t=o.inspections_summary.date;break;case"details-of-tested-cases":title=this.$t("検査実施状況"),t=o.inspection_status_summary.date;break;case"number-of-confirmed-cases":title=this.$t("陽性患者数"),t=o.patients.date;break;case"attributes-of-confirmed-cases":title=this.$t("陽性患者の属性"),t=o.patients.date;break;case"number-of-tested":title=this.$t("検査実施件数"),t=o.inspections_summary.date;break;case"number-of-inspection-persons":title=this.$t("検査実施人数"),t=o.inspection_persons.date;break;case"number-of-reports-to-covid19-telephone-advisory-center":title=this.$t("新型コロナコールセンター相談件数"),t=o.contacts.date;break;case"number-of-reports-to-covid19-consultation-desk":title=this.$t("新型コロナ受診相談窓口相談件数"),t=o.querents.date;break;case"predicted-number-of-toei-subway-passengers":title=this.$t("都営地下鉄の利用者数の推移"),t=n.date;break;case"agency":title=this.$t("都庁来庁者数の推移"),t=c.date}var data={title:title,updatedAt:t};return data},head:function(){var t="https://stopcovid19.metro.tokyo.lg.jp",e=(new Date).getTime(),r="ja"===this.$i18n.locale?"".concat(t,"/ogp/").concat(this.$route.params.card,".png?t=").concat(e):"".concat(t,"/ogp/").concat(this.$i18n.locale,"/").concat(this.$route.params.card,".png?t=").concat(e),o="".concat(this.updatedAt," | ").concat(this.$t("当サイトは新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供するために、有志が東京都のサイトを基に開発したものです。"));return{title:this.title,meta:[{hid:"og:url",property:"og:url",content:t+this.$route.path+"/"},{hid:"og:title",property:"og:title",content:this.title+" | "+this.$t("葛飾区")+" "+this.$t("新型コロナウイルス感染症")+this.$t("対策サイト(非公式)")},{hid:"description",name:"description",content:o},{hid:"og:description",property:"og:description",content:o},{hid:"og:image",property:"og:image",content:r},{hid:"twitter:image",name:"twitter:image",content:r}]}}},f=r(5),component=Object(f.a)(h,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",["details-of-confirmed-cases"==this.$route.params.card?e("confirmed-cases-details-card"):"details-of-tested-cases"==this.$route.params.card?e("tested-cases-details-card"):"number-of-confirmed-cases"==this.$route.params.card?e("confirmed-cases-number-card"):"attributes-of-confirmed-cases"==this.$route.params.card?e("confirmed-cases-attributes-card"):"number-of-tested"==this.$route.params.card?e("tested-number-card"):"number-of-inspection-persons"==this.$route.params.card?e("inspection-persons-number-card"):"number-of-reports-to-covid19-telephone-advisory-center"==this.$route.params.card?e("telephone-advisory-reports-number-card"):"number-of-reports-to-covid19-consultation-desk"==this.$route.params.card?e("consultation-desk-reports-number-card"):"predicted-number-of-toei-subway-passengers"==this.$route.params.card?e("metro-card"):"agency"==this.$route.params.card?e("agency-card"):this._e()],1)}),[],!1,null,null,null);e.default=component.exports}}]);