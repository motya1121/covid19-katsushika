(window.webpackJsonp=window.webpackJsonp||[]).push([[10],{290:function(t,e,n){"use strict";var r=n(1),o=n(106),l=r.a.extend({props:{title:{type:String,default:""},titleId:{type:String,default:""},date:{type:String,default:""},loading:{type:Boolean,required:!1,default:!1}},data:function(){return{openGraphEmbed:!1,displayShare:!1,showOverlay:!1}},computed:{formattedDate:function(){return Object(o.d)(this.date)},graphEmbedValue:function(){var t='<iframe width="560" height="315" src="'+this.permalink(!0,!0)+'" frameborder="0"></iframe>';return t}},watch:{displayShare:function(t){t?document.documentElement.addEventListener("click",this.toggleShareMenu):document.documentElement.removeEventListener("click",this.toggleShareMenu)}},methods:{toggleShareMenu:function(t){t.stopPropagation(),this.displayShare=!this.displayShare},closeShareMenu:function(){this.displayShare=!1},isCopyAvailable:function(){return!!navigator.clipboard},copyEmbedCode:function(){var t=this;navigator.clipboard.writeText(this.graphEmbedValue).then((function(){t.closeShareMenu(),t.showOverlay=!0,setTimeout((function(){t.showOverlay=!1}),2e3)}))},stopClosingShareMenu:function(t){t.stopPropagation()},permalink:function(){var t=arguments.length>0&&void 0!==arguments[0]&&arguments[0],embed=arguments.length>1&&void 0!==arguments[1]&&arguments[1],e="/cards/"+this.titleId;return embed&&(e+="?embed=true"),e=this.localePath(e),t&&(e=location.protocol+"//"+location.host+e),e},twitter:function(){var t="https://twitter.com/intent/tweet?text="+this.title+" / "+this.$t("葛飾区")+this.$t("新型コロナウイルス感染症")+this.$t("対策サイト(非公式)")+"&url="+this.permalink(!0)+"&hashtags=StopCovid19JP";window.open(t)},facebook:function(){var t="https://www.facebook.com/sharer.php?u="+this.permalink(!0);window.open(t)},line:function(){var t="https://social-plugins.line.me/lineit/share?url="+this.permalink(!0);window.open(t)}}}),c=(n(425),n(5)),d=n(38),h=n.n(d),f=n(511),v=n(523),m=n(277),component=Object(c.a)(l,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-card",{staticClass:"DataView",attrs:{loading:t.loading}},[n("div",{staticClass:"DataView-Inner"},[n("div",{staticClass:"DataView-Header"},[n("h3",{staticClass:"DataView-Title",class:t.$slots.infoPanel?"with-infoPanel":""},[t._v("\n        "+t._s(t.title)+"\n      ")]),t._v(" "),t._t("infoPanel")],2),t._v(" "),n("div",{staticClass:"DataView-Description"},[t._t("description")],2),t._v(" "),n("div",[t._t("button")],2),t._v(" "),n("div",{staticClass:"DataView-CardText"},[t._t("default")],2),t._v(" "),n("div",{staticClass:"DataView-Description"},[t._t("footer-description")],2),t._v(" "),n("div",{staticClass:"DataView-Footer"},[n("div",{staticClass:"Footer-Left"},[t._t("footer"),t._v(" "),n("div",[n("a",{staticClass:"Permalink",attrs:{href:t.permalink()}},[n("time",{attrs:{datetime:t.formattedDate}},[t._v("\n              "+t._s(t.$t("{date} 更新",{date:t.date}))+"\n            ")])])])],2),t._v(" "),"true"!=this.$route.query.embed?n("div",{staticClass:"Footer-Right"},[n("button",{staticClass:"DataView-Share-Opener",on:{click:t.toggleShareMenu}},[n("svg",{attrs:{width:"14",height:"16",viewBox:"0 0 14 16",fill:"none",xmlns:"http://www.w3.org/2000/svg",role:"img","aria-label":t.$t("{title}のグラフをシェア",{title:t.title})}},[n("path",{attrs:{"fill-rule":"evenodd","clip-rule":"evenodd",d:"M7.59999 3.5H9.5L7 0.5L4.5 3.5H6.39999V11H7.59999V3.5ZM8.5 5.75H11.5C11.9142 5.75 12.25 6.08579 12.25 6.5V13.5C12.25 13.9142 11.9142 14.25 11.5 14.25H2.5C2.08579 14.25 1.75 13.9142 1.75 13.5V6.5C1.75 6.08579 2.08579 5.75 2.5 5.75H5.5V4.5H2.5C1.39543 4.5 0.5 5.39543 0.5 6.5V13.5C0.5 14.6046 1.39543 15.5 2.5 15.5H11.5C12.6046 15.5 13.5 14.6046 13.5 13.5V6.5C13.5 5.39543 12.6046 4.5 11.5 4.5H8.5V5.75Z",fill:"#808080"}})])]),t._v(" "),t.displayShare?n("div",{staticClass:"DataView-Share-Buttons py-2",on:{click:t.stopClosingShareMenu}},[n("div",{staticClass:"Close-Button"},[n("v-icon",{attrs:{"aria-label":t.$t("閉じる")},on:{click:t.closeShareMenu}},[t._v("\n              mdi-close\n            ")])],1),t._v(" "),n("h4",[t._v(t._s(t.$t("埋め込み用コード")))]),t._v(" "),n("div",{staticClass:"EmbedCode"},[t.isCopyAvailable()?n("v-icon",{staticClass:"EmbedCode-Copy",attrs:{"aria-label":t.$t("クリップボードにコピー")},on:{click:t.copyEmbedCode}},[t._v("\n              mdi-clipboard-outline\n            ")]):t._e(),t._v("\n            "+t._s(t.graphEmbedValue)+"\n          ")],1),t._v(" "),n("div",{staticClass:"Buttons"},[n("button",{attrs:{"aria-label":t.$t("LINEで{title}のグラフをシェア",{title:t.title})},on:{click:t.line}},[n("picture",[n("source",{staticClass:"icon-resize line",attrs:{srcset:"/line.webp",type:"image/webp"}}),t._v(" "),n("img",{staticClass:"icon-resize line",attrs:{src:"/line.png",alt:"LINE"}})])]),t._v(" "),n("button",{attrs:{"aria-label":t.$t("Twitterで{title}のグラフをシェア",{title:t.title})},on:{click:t.twitter}},[n("picture",[n("source",{staticClass:"icon-resize twitter",attrs:{srcset:"/twitter.webp",type:"image/webp"}}),t._v(" "),n("img",{staticClass:"icon-resize twitter",attrs:{src:"/twitter.png",alt:"Twitter"}})])]),t._v(" "),n("button",{attrs:{"aria-label":t.$t("facebookで{title}のグラフをシェア",{title:t.title})},on:{click:t.facebook}},[n("picture",[n("source",{staticClass:"icon-resize facebook",attrs:{srcset:"/facebook.webp",type:"image/webp"}}),t._v(" "),n("img",{staticClass:"icon-resize facebook",attrs:{src:"/facebook.png",alt:"facebook"}})])])])]):t._e()]):t._e()])]),t._v(" "),t.showOverlay?n("div",{staticClass:"overlay"},[n("div",{staticClass:"overlay-text"},[t._v("\n      "+t._s(t.$t("埋め込みコードをコピーしました"))+"\n    ")]),t._v(" "),n("v-footer",{staticClass:"DataView-Footer"},[n("time",{attrs:{datetime:t.date}},[t._v(t._s(t.$t("{date} 更新",{date:t.date})))]),t._v(" "),t._t("footer")],2)],1):t._e()])}),[],!1,null,null,null);e.a=component.exports;h()(component,{VCard:f.a,VFooter:v.a,VIcon:m.a})},295:function(t,e,n){"use strict";e.a=function(data){var t=[],e=new Date,n=0;return data.filter((function(t){return new Date(t["日付"])<e})).forEach((function(e){var r=new Date(e["日付"]),o=e["小計"];isNaN(o)||(n+=o,t.push({label:"".concat(r.getMonth()+1,"/").concat(r.getDate()),transition:o,cumulative:n}))})),t}},299:function(t,e,n){"use strict";n.d(e,"a",(function(){return c}));var r={strokeColor:"#5a8055",fillColor:"#1b4d30"},o={strokeColor:"#5a8055",fillColor:"#00a040"},l={strokeColor:"#5a8055",fillColor:"#c5e2c6"};function c(t){switch(t){case 1:return[o];case 2:return[r,l];default:return[r,o,l]}}},301:function(t,e,n){"use strict";var r=n(1).a.extend({props:{lText:{type:String,required:!0},sText:{type:String,required:!0},unit:{type:String,required:!0}}}),o=(n(445),n(5)),component=Object(o.a)(r,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"DataView-DataInfo"},[n("span",{staticClass:"DataView-DataInfo-summary"},[t._v("\n    "+t._s(t.lText)+"\n    "),n("small",{staticClass:"DataView-DataInfo-summary-unit"},[t._v(t._s(t.unit))])]),t._v(" "),n("br"),t._v(" "),n("small",{staticClass:"DataView-DataInfo-date"},[t._v(t._s(t.sText))])])}),[],!1,null,null,null);e.a=component.exports},302:function(t,e,n){"use strict";n(437);var r=n(130),o=(n(32),n(1)),l=n(290),c=n(360),d=n(301),h=n(361),f=n(123),v=n(299),m={created:function(){this.canvas=!0,this.dataKind=this.$route.query.embed&&"cumulative"===this.$route.query.dataKind?"cumulative":"transition"},components:{DataView:l.a,DataSelector:c.a,DataViewBasicInfoPanel:d.a,OpenDataLink:h.a},props:{title:{type:String,default:""},titleId:{type:String,default:""},chartId:{type:String,default:"time-bar-chart"},chartData:{type:Array,default:function(){return[]}},date:{type:String,required:!0},unit:{type:String,default:""},url:{type:String,default:""},scrollPlugin:{type:Array,default:function(){return f.b}},yAxesBgPlugin:{type:Array,default:function(){return f.c}}},data:function(){return{dataKind:"transition",chartWidth:null,canvas:!0}},computed:{displayCumulativeRatio:function(){var t=this.chartData.slice(-1)[0].cumulative,e=this.chartData.slice(-2)[0].cumulative;return this.formatDayBeforeRatio(t-e)},displayTransitionRatio:function(){var t=this.chartData.slice(-1)[0].transition,e=this.chartData.slice(-2)[0].transition;return this.formatDayBeforeRatio(t-e)},displayInfo:function(){return"transition"===this.dataKind?{lText:"".concat(this.chartData.slice(-1)[0].transition.toLocaleString()),sText:"".concat(this.chartData.slice(-1)[0].label," ").concat(this.$t("実績値"),"（").concat(this.$t("前日比"),": ").concat(this.displayTransitionRatio," ").concat(this.unit,"）"),unit:this.unit}:{lText:this.chartData[this.chartData.length-1].cumulative.toLocaleString(),sText:"".concat(this.chartData.slice(-1)[0].label," ").concat(this.$t("累計値"),"（").concat(this.$t("前日比"),": ").concat(this.displayCumulativeRatio," ").concat(this.unit,"）"),unit:this.unit}},displayData:function(){var style=Object(v.a)(1)[0];return"transition"===this.dataKind?{labels:this.chartData.map((function(t){return t.label})),datasets:[{label:this.dataKind,data:this.chartData.map((function(t){return t.transition})),backgroundColor:style.fillColor,borderColor:style.strokeColor,borderWidth:1}]}:{labels:this.chartData.map((function(t){return t.label})),datasets:[{label:this.dataKind,data:this.chartData.map((function(t){return t.cumulative})),backgroundColor:style.fillColor,borderColor:style.strokeColor,borderWidth:1}]}},displayOption:function(){var t=this.unit,e={tooltips:{displayColors:!1,callbacks:{label:function(e){return"".concat(parseInt(e.value).toLocaleString()," ").concat(t)},title:function(t,data){return data.labels[t[0].index]}}},responsive:!1,maintainAspectRatio:!1,legend:{display:!1},scales:{xAxes:[{id:"day",stacked:!0,gridLines:{display:!1},ticks:{fontSize:9,maxTicksLimit:20,fontColor:"#808080",maxRotation:0,callback:function(label){return label.split("/")[1]}}},{id:"month",stacked:!0,gridLines:{drawOnChartArea:!1,drawTicks:!0,drawBorder:!1,tickMarkLength:10},ticks:{fontSize:11,fontColor:"#808080",padding:3,fontStyle:"bold"},type:"time",time:{unit:"month",parser:"M/D",displayFormats:{month:"MMM"}}}],yAxes:[{stacked:!0,gridLines:{display:!0,color:"#E5E5E5"},ticks:{suggestedMin:0,maxTicksLimit:8,fontColor:"#808080",suggestedMax:this.scaledTicksYAxisMax}}]}};return"true"===this.$route.query.ogp&&Object.assign(e,{animation:{duration:0}}),e},displayDataHeader:function(){return"transition"===this.dataKind?{labels:["2020/1/1"],datasets:[{data:[Math.max.apply(Math,Object(r.a)(this.chartData.map((function(t){return t.transition}))))],backgroundColor:"transparent",borderWidth:0}]}:{labels:["2020/1/1"],datasets:[{data:[Math.max.apply(Math,Object(r.a)(this.chartData.map((function(t){return t.cumulative}))))],backgroundColor:"transparent",borderWidth:0}]}},displayOptionHeader:function(){return{responsive:!1,maintainAspectRatio:!1,legend:{display:!1},tooltips:{enabled:!1},scales:{xAxes:[{id:"day",stacked:!0,gridLines:{display:!1},ticks:{fontSize:9,maxTicksLimit:20,fontColor:"transparent",maxRotation:0,minRotation:0,callback:function(label){return label.split("/")[1]}}},{id:"month",stacked:!0,gridLines:{drawOnChartArea:!1,drawTicks:!1,drawBorder:!1,tickMarkLength:10},ticks:{fontSize:11,fontColor:"transparent",padding:13,fontStyle:"bold",callback:function(label){return["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].indexOf(label.split(" ")[0])+1+"月"}},type:"time",time:{unit:"month"}}],yAxes:[{stacked:!0,gridLines:{display:!0,drawOnChartArea:!1,color:"#E5E5E5"},ticks:{suggestedMin:0,maxTicksLimit:8,fontColor:"#808080",suggestedMax:this.scaledTicksYAxisMax}}]},animation:{duration:0}}},scaledTicksYAxisMax:function(){var t="transition"===this.dataKind?"transition":"cumulative",e=this.chartData.map((function(e){return e[t]}));return Math.max.apply(Math,Object(r.a)(e))},tableHeaders:function(){return[{text:this.$t("日付"),value:"text"},{text:this.title,value:"0"}]},tableData:function(){var t=this;return this.displayData.datasets[0].data.map((function(e,i){return{text:t.displayData.labels[i],0:t.displayData.datasets[0].data[i]}}))}},methods:{formatDayBeforeRatio:function(t){var e=t.toLocaleString();switch(Math.sign(t)){case 1:return"+".concat(e);case-1:default:return"".concat(e)}}},mounted:function(){this.$el&&(this.chartWidth=(this.$el.clientWidth-44-38)/60*this.displayData.labels.length+38,this.chartWidth=Math.max(this.$el.clientWidth-44,this.chartWidth));var canvas=this.$refs.barChart.$el.querySelector("canvas"),t="".concat(this.titleId,"-graph");canvas&&(canvas.setAttribute("role","img"),canvas.setAttribute("aria-labelledby",t))}},x=o.a.extend(m),w=n(5),_=n(38),y=n.n(_),D=n(516),component=Object(w.a)(x,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("data-view",{attrs:{title:t.title,"title-id":t.titleId,date:t.date},scopedSlots:t._u([{key:"description",fn:function(){return[t._t("description")]},proxy:!0},{key:"button",fn:function(){return[n("data-selector",{style:{display:t.canvas?"inline-block":"none"},attrs:{"target-id":t.chartId},model:{value:t.dataKind,callback:function(e){t.dataKind=e},expression:"dataKind"}})]},proxy:!0},{key:"infoPanel",fn:function(){return[n("data-view-basic-info-panel",{attrs:{"l-text":t.displayInfo.lText,"s-text":t.displayInfo.sText,unit:t.displayInfo.unit}})]},proxy:!0}],null,!0)},[t._v(" "),t._v(" "),n("h4",{staticClass:"visually-hidden",attrs:{id:t.titleId+"-graph"}},[t._v("\n    "+t._s(t.$t("{title}のグラフ",{title:t.title}))+"\n  ")]),t._v(" "),n("div",{staticClass:"LegendStickyChart"},[n("div",{staticClass:"scrollable",style:{display:t.canvas?"block":"none"}},[n("div",{style:{width:t.chartWidth+"px"}},[n("bar",{ref:"barChart",attrs:{"chart-id":t.chartId,"chart-data":t.displayData,options:t.displayOption,plugins:t.scrollPlugin,height:240,width:t.chartWidth}})],1)]),t._v(" "),n("bar",{staticClass:"sticky-legend",style:{display:t.canvas?"block":"none"},attrs:{"chart-id":t.chartId+"-header","chart-data":t.displayDataHeader,options:t.displayOptionHeader,plugins:t.yAxesBgPlugin,height:240,width:t.chartWidth}})],1),t._v(" "),n("v-data-table",{staticClass:"cardTable",style:{top:"-9999px",position:t.canvas?"fixed":"static"},attrs:{headers:t.tableHeaders,items:t.tableData,"items-per-page":-1,"hide-default-footer":!0,height:240,"fixed-header":!0,"disable-sort":!0,"mobile-breakpoint":0,"item-key":"name"},scopedSlots:t._u([{key:"body",fn:function(e){var r=e.items;return[n("tbody",t._l(r,(function(e){return n("tr",{key:e.text},[n("th",{staticClass:"text-start"},[t._v(t._s(e.text))]),t._v(" "),n("td",{staticClass:"text-start"},[t._v(t._s(e[0]))])])})),0)]}}])})],1)}),[],!1,null,null,null);e.a=component.exports;y()(component,{VDataTable:D.a})},328:function(t,e,n){var content=n(419);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("97e7ab7c",content,!0,{sourceMap:!1})},331:function(t,e,n){var content=n(426);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("4d5720d6",content,!0,{sourceMap:!1})},332:function(t,e,n){var content=n(434);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("4b30e3a2",content,!0,{sourceMap:!1})},333:function(t,e,n){var content=n(436);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("7730958c",content,!0,{sourceMap:!1})},334:function(t,e,n){var content=n(439);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("970c2a6c",content,!0,{sourceMap:!1})},335:function(t,e,n){var content=n(446);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("e3e1d1b4",content,!0,{sourceMap:!1})},336:function(t,e,n){var content=n(448);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("08457358",content,!0,{sourceMap:!1})},337:function(t,e,n){var content=n(489);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(14).default)("435e5f58",content,!0,{sourceMap:!1})},358:function(t,e,n){"use strict";n(60),n(61),n(6),n(56),n(15),n(7);var r=n(104),o=n(295),l=n(9),c=n.n(l),d=[{text:"公表日",value:"公表日"},{text:"居住地",value:"居住地"},{text:"年代",value:"年代"},{text:"性別",value:"性別"},{text:"状態",value:"状態"},{text:"退院※",value:"退院",align:"center"}],h=n(1),f=n(290),v=n(301),m=n(361),x=h.a.extend({components:{DataView:f.a,DataViewBasicInfoPanel:v.a,OpenDataLink:m.a},props:{title:{type:String,default:""},titleId:{type:String,default:""},chartData:{type:Object,default:function(){}},date:{type:String,default:""},info:{type:Object,default:function(){}},url:{type:String,default:""},customSort:{type:Function,default:function(t,e,n){return t.sort((function(a,b){var t=0;return String(a[e[0]])<String(b[e[0]])?t=-1:String(b[e[0]])<String(a[e[0]])&&(t=1),0!==t&&(t=n[0]?-1*t:t),t})),t}}},mounted:function(){this.$refs.displayedTable.$el.querySelectorAll("table").forEach((function(table){table.setAttribute("tabindex","0")}))}}),w=(n(488),n(5)),_=n(38),y=n.n(_),D=n(516),component=Object(w.a)(x,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("data-view",{attrs:{title:t.title,"title-id":t.titleId,date:t.date},scopedSlots:t._u([{key:"button",fn:function(){return[n("span")]},proxy:!0},{key:"infoPanel",fn:function(){return[n("data-view-basic-info-panel",{attrs:{"l-text":t.info.lText,"s-text":t.info.sText,unit:t.info.unit}})]},proxy:!0}])},[t._v(" "),n("v-data-table",{ref:"displayedTable",staticClass:"cardTable",attrs:{headers:t.chartData.headers,items:t.chartData.datasets,"items-per-page":-1,"hide-default-footer":!0,height:240,"fixed-header":!0,"mobile-breakpoint":0,"custom-sort":t.customSort},scopedSlots:t._u([{key:"body",fn:function(e){var r=e.items;return[n("tbody",t._l(r,(function(e){return n("tr",{key:e.text},[n("th",{staticClass:"text-start"},[t._v(t._s(e["公表日"]))]),t._v(" "),n("td",{staticClass:"text-start"},[t._v(t._s(e["居住地"]))]),t._v(" "),n("td",{staticClass:"text-start"},[t._v(t._s(e["年代"]))]),t._v(" "),n("td",{staticClass:"text-start"},[t._v(t._s(e["性別"]))]),t._v(" "),n("td",{staticClass:"text-start"},[t._v(t._s(e["状態"]))]),t._v(" "),n("td",{staticClass:"text-center"},[t._v(t._s(e["退院"]))])])})),0)]}}])}),t._v(" "),n("div",{staticClass:"note"},[t._v("\n    "+t._s(t.$t("※退院には、死亡退院を含む"))+"\n  ")])],1)}),[],!1,null,null,null),C=component.exports;y()(component,{VDataTable:D.a});var k={components:{DataTable:C},data:function(){var t=Object(o.a)(r.patients_summary.data),e=function(data){var t={headers:d,datasets:[]};return data.forEach((function(e){var n,r,o,l,d={"公表日":null!==(n=c()(e["リリース日"]).format("MM/DD"))&&void 0!==n?n:"不明","居住地":null!==(r=e["居住地"])&&void 0!==r?r:"調査中","年代":null!==(o=e["年代"])&&void 0!==o?o:"不明","性別":null!==(l=e["性別"])&&void 0!==l?l:"不明","退院":e["退院"],"状態":e["状態"]};t.datasets.push(d)})),t.datasets.sort((function(a,b){return a.公表日===b.公表日?0:a.公表日<b.公表日?1:-1})),t}(r.patients.data),n={lText:t[t.length-1].cumulative.toLocaleString(),sText:this.$t("{date}の累計",{date:t[t.length-1].label}),unit:this.$t("人")},l=!0,h=!1,f=void 0;try{for(var v,m=e.headers[Symbol.iterator]();!(l=(v=m.next()).done);l=!0){var header=v.value;header.text="退院"===header.value?this.$t("退院※"):this.$t(header.value)}}catch(t){h=!0,f=t}finally{try{l||null==m.return||m.return()}finally{if(h)throw f}}var x=!0,w=!1,_=void 0;try{for(var y,D=e.datasets[Symbol.iterator]();!(x=(y=D.next()).done);x=!0){var C=y.value;if(C["居住地"]=this.getTranslatedWording(C["居住地"]),C["性別"]=this.getTranslatedWording(C["性別"]),C["退院"]=this.getTranslatedWording(C["退院"]),"代"===C["年代"].substr(-1,1)){var k=C["年代"].substring(0,2);C["年代"]=this.$t("{age}代",{age:k})}else C["年代"]=this.$t(C["年代"])}}catch(t){w=!0,_=t}finally{try{x||null==D.return||D.return()}finally{if(w)throw _}}var data={Data:r,patientsTable:e,sumInfoOfPatients:n};return data},methods:{getTranslatedWording:function(t){return"-"===t||"‐"===t||"―"===t||null==t?t:this.$t(t)},customSort:function(t,e,n){var r=this.$t("10歳未満").toString();return t.sort((function(a,b){if(a[e[0]]===b[e[0]])return 0;var t=0;return t="年代"!==e[0]||a[e[0]]!==r&&b[e[0]]!==r?String(a[e[0]])<String(b[e[0]])?-1:1:a[e[0]]===r?-1:1,n[0]?-1*t:t})),t}}},V=n(512),S=Object(w.a)(k,(function(){var t=this.$createElement,e=this._self._c||t;return e("v-col",{staticClass:"DataCard",attrs:{cols:"12",md:"6"}},[e("data-table",{attrs:{title:this.$t("陽性患者の属性"),"title-id":"attributes-of-confirmed-cases","chart-data":this.patientsTable,"chart-option":{},date:this.Data.patients.date,info:this.sumInfoOfPatients,"custom-sort":this.customSort}})],1)}),[],!1,null,null,null);e.a=S.exports;y()(S,{VCol:V.a})},359:function(t,e,n){"use strict";var r=n(104),o=n(290),l=(n(60),n(61),n(6),n(103),n(1).a.extend({props:{"検査実施人数":{type:Number,required:!0},"陽性者数":{type:Number,required:!0},"入院調整中":{type:Number,required:!0},"入院中":{type:Number,required:!0},"宿泊療養中":{type:Number,required:!0},"自宅療養中":{type:Number,required:!0},"死亡":{type:Number,required:!0},"退院":{type:Number,required:!0}},methods:{getAdjustX:function(input){switch(input.toString(10).length){case 1:return 3;case 2:return 0;case 3:return-3;case 4:return-8;default:return 0}}}})),c=n(433),d=n(5);var h=Object(d.a)(l,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("ul",{class:t.$style.container},[n("li",{class:[t.$style.box,t.$style.parent]},[n("div",{class:t.$style.content},[n("span",[t._v(" "+t._s(t.$t("陽性者数"))+" ("+t._s(t.$t("累計"))+") ")]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.陽性者数.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])]),t._v(" "),n("ul",{class:t.$style.group},[n("li",{class:[t.$style.box]},[n("div",{class:t.$style.content},[n("span",[t._v(t._s(t.$t("入院調整中")))]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.入院調整中.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])])]),t._v(" "),n("li",{class:[t.$style.box]},[n("div",{class:t.$style.content},[n("span",[t._v(t._s(t.$t("入院中")))]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.入院中.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])])]),t._v(" "),n("li",{class:[t.$style.box]},[n("div",{class:t.$style.content},[n("span",[t._v(t._s(t.$t("宿泊療養中")))]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.宿泊療養中.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])])]),t._v(" "),n("li",{class:[t.$style.box]},[n("div",{class:t.$style.content},[n("span",[t._v(t._s(t.$t("自宅療養中")))]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.自宅療養中.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])])]),t._v(" "),n("li",{class:[t.$style.box]},[n("div",{class:t.$style.content},[n("span",[t._v(t._s(t.$t("死亡")))]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.死亡.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])])]),t._v(" "),n("li",{class:[t.$style.box]},[n("div",{class:t.$style.content},[n("span",[t._v(t._s(t.$t("退院")))]),t._v(" "),n("span",[n("strong",[t._v(t._s(t.退院.toLocaleString()))]),t._v(" "),n("span",{class:t.$style.unit},[t._v(t._s(t.$t("人")))])])])])])])])}),[],!1,(function(t){this.$style=c.default.locals||c.default}),null,null).exports,f={components:{DataView:o.a,ConfirmedCasesDetailsTable:h},data:function(){var t=function(data){return{"検査実施人数":data.value,"陽性者数":data.children[0].value,"入院調整中":data.children[0].children[0].value,"入院中":data.children[0].children[1].value,"宿泊療養中":data.children[0].children[2].value,"自宅療養中":data.children[0].children[3].value,"死亡":data.children[0].children[4].value,"退院":data.children[0].children[5].value}}(r.main_summary),data={Data:r,confirmedCases:t};return data}},v=n(435),m=n(38),x=n.n(m),w=n(512);var _=Object(d.a)(f,(function(){var t=this.$createElement,e=this._self._c||t;return e("v-col",{staticClass:"DataCard",attrs:{cols:"12",md:"6"}},[e("data-view",{attrs:{title:this.$t("感染者の状況"),"title-id":"details-of-confirmed-cases",date:this.Data.patients.date}},[e("confirmed-cases-details-table",this._b({attrs:{"aria-label":this.$t("感染者の状況")}},"confirmed-cases-details-table",this.confirmedCases,!1))],1)],1)}),[],!1,(function(t){this.$style=v.default.locals||v.default}),null,null);e.a=_.exports;x()(_,{VCol:w.a})},360:function(t,e,n){"use strict";var r=n(1).a.extend({name:"DataSelector",props:{value:{type:String,default:"transition"},targetId:{type:String,default:function(t){return t&&""!==t?t:null}}}}),o=(n(438),n(5)),l=n(38),c=n.n(l),d=n(364),h=n(524),f=n(444),v=n.n(f),m=n(289),component=Object(o.a)(r,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-btn-toggle",{staticClass:"DataSelector",attrs:{"aria-controls":t.targetId,value:t.value,mandatory:""},on:{change:function(e){return t.$emit("input",e)}}},[n("v-btn",{directives:[{name:"ripple",rawName:"v-ripple",value:!1,expression:"false"}],staticClass:"DataSelector-Button",attrs:{"aria-pressed":"transition"===t.value?"true":"false",value:"transition"}},[t._v("\n    "+t._s(t.$t("日別"))+"\n  ")]),t._v(" "),n("v-btn",{directives:[{name:"ripple",rawName:"v-ripple",value:!1,expression:"false"}],staticClass:"DataSelector-Button",attrs:{"aria-pressed":"cumulative"===t.value?"true":"false",value:"cumulative"}},[t._v("\n    "+t._s(t.$t("累計"))+"\n  ")])],1)}),[],!1,null,null,null);e.a=component.exports;c()(component,{VBtn:d.a,VBtnToggle:h.a}),v()(component,{Ripple:m.a})},361:function(t,e,n){"use strict";var r=n(1).a.extend({props:{url:{type:String,default:""}}}),o=(n(447),n(5)),l=n(38),c=n.n(l),d=n(277),component=Object(o.a)(r,(function(){var t=this.$createElement,e=this._self._c||t;return e("a",{staticClass:"OpenDataLink",attrs:{href:this.url,target:"_blank",rel:"noopener noreferrer"}},[this._v("\n  "+this._s(this.$t("オープンデータを入手"))+"\n  "),e("v-icon",{staticClass:"ExternalLinkIcon",attrs:{size:"15","aria-label":this.$t("別タブで開く"),role:"img","aria-hidden":!1}},[this._v("\n    mdi-open-in-new\n  ")])],1)}),[],!1,null,null,null);e.a=component.exports;c()(component,{VIcon:d.a})},362:function(t,e,n){"use strict";var r=n(104),o=n(295),l={components:{TimeBarChart:n(302).a},data:function(){var t=Object(o.a)(r.patients_summary.data),data={Data:r,patientsGraph:t};return data}},c=n(5),d=n(38),h=n.n(d),f=n(512),component=Object(c.a)(l,(function(){var t=this.$createElement,e=this._self._c||t;return e("v-col",{staticClass:"DataCard",attrs:{cols:"12",md:"6"}},[e("time-bar-chart",{attrs:{title:this.$t("陽性患者数"),"title-id":"number-of-confirmed-cases","chart-id":"time-bar-chart-patients","chart-data":this.patientsGraph,date:this.Data.patients.date,unit:this.$t("人")}})],1)}),[],!1,null,null,null);e.a=component.exports;h()(component,{VCol:f.a})},363:function(t,e,n){"use strict";var r=n(1).a.extend({props:{url:{type:String,default:""},label:{type:String,default:""}}}),o=(n(418),n(5)),l=n(38),c=n.n(l),d=n(277),component=Object(o.a)(r,(function(){var t=this.$createElement,e=this._self._c||t;return e("a",{staticClass:"ExternalLink",attrs:{href:this.url,target:"_blank",rel:"noopener noreferrer"}},[this._v("\n  "+this._s(this.label)+"\n  "),e("v-icon",{staticClass:"ExternalLinkIcon",attrs:{size:"15","aria-label":this.$t("別タブで開く"),role:"img","aria-hidden":!1}},[this._v("\n    mdi-open-in-new\n  ")])],1)}),[],!1,null,null,null);e.a=component.exports;c()(component,{VIcon:d.a})},418:function(t,e,n){"use strict";var r=n(328);n.n(r).a},419:function(t,e,n){(e=n(13)(!1)).push([t.i,".ExternalLink{text-decoration:none}.ExternalLink .ExternalLinkIcon{vertical-align:text-bottom}",""]),t.exports=e},425:function(t,e,n){"use strict";var r=n(331);n.n(r).a},426:function(t,e,n){(e=n(13)(!1)).push([t.i,".DataView{background-color:#fff;box-shadow:0 0 2px rgba(0,0,0,.15);border:.5px solid #d9d9d9 !important;border-radius:4px;height:100%}.DataView .LegendStickyChart{margin:16px 0;position:relative;overflow:hidden}.DataView .LegendStickyChart .scrollable{overflow-x:scroll}.DataView .LegendStickyChart .scrollable::-webkit-scrollbar{height:4px;background-color:rgba(0,0,0,.01)}.DataView .LegendStickyChart .scrollable::-webkit-scrollbar-thumb{background-color:rgba(0,0,0,.07)}.DataView .LegendStickyChart .sticky-legend{position:absolute;top:0;pointer-events:none}.DataView-Header{display:flex;align-items:flex-start;flex-flow:column;padding:0 10px}@media screen and (min-width: 769px){.DataView-Header{padding:0 5px}}@media screen and (min-width: 1171px){.DataView-Header{width:100%;flex-flow:row;flex-wrap:wrap;padding:0}}.DataView-DataInfo-summary{color:#4d4d4d;font-family:Hiragino Sans,sans-serif;font-style:normal;font-size:30px;line-height:30px;white-space:nowrap}.DataView-DataInfo-summary-unit{font-size:.6em;width:100%}.DataView-DataInfo-date{font-size:12px;line-height:12px;color:#707070;width:100%;display:inline-block}.DataView-Inner{display:flex;flex-flow:column;justify-content:space-between;padding:22px;height:100%}.DataView-Title{width:100%;margin-bottom:10px;font-size:1.25rem;line-height:1.5;font-weight:normal;color:#4d4d4d}@media screen and (min-width: 1171px){.DataView-Title{margin-bottom:0}.DataView-Title.with-infoPanel{width:50%}}.DataView-CardText{margin:16px 0}.DataView-Description{margin:10px 0 0;font-size:12px;color:#707070}.DataView-Description ul,.DataView-Description ol{list-style-type:none;padding:0}.DataView-Footer{font-size:12px;font-size:0.75rem;padding:0 !important;display:flex;justify-content:space-between;color:#707070 !important;text-align:right;background-color:#fff !important}.DataView-Footer .Permalink{color:#707070 !important}.DataView-Footer .OpenDataLink{text-decoration:none}.DataView-Footer .OpenDataLink .ExternalLinkIcon{vertical-align:text-bottom}.DataView-Footer .Footer-Left{text-align:left}.DataView-Footer .Footer-Right{position:relative;display:flex;align-items:flex-end}.DataView-Footer .Footer-Right .DataView-Share-Opener{cursor:pointer;margin-right:6px}.DataView-Footer .Footer-Right .DataView-Share-Opener>svg{width:auto !important}.DataView-Footer .Footer-Right .DataView-Share-Opener:focus{outline:dotted #707070 1px}.DataView-Footer .Footer-Right .DataView-Share-Buttons{position:absolute;padding:8px;right:-4px;bottom:1.5em;width:240px;border:solid 1px #d9d9d9;background:#fff !important;border-radius:8px;text-align:left;font-size:1rem;z-index:2}.DataView-Footer .Footer-Right .DataView-Share-Buttons>*{padding:4px 0}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Close-Button{display:flex;justify-content:flex-end;color:#707070}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Close-Button button{border-radius:50%;border:1px solid #fff}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Close-Button button:focus{border:1px dotted #707070;outline:none}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.EmbedCode{position:relative;padding:4px;padding-right:30px;color:#030303;border:solid 1px #eee;border-radius:8px;font-size:12px}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.EmbedCode .EmbedCode-Copy{position:absolute;top:.3em;right:.3em;color:#707070}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.EmbedCode button{border-radius:50%;border:solid 1px #eee}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.EmbedCode button:focus{border:1px dotted #707070;outline:none}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons{display:flex;justify-content:center;margin-top:4px}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons .icon-resize{border-radius:50%;font-size:30px}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons .icon-resize.twitter{color:#fff;background:#2a96eb}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons .icon-resize.facebook{color:#364e8a}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons .icon-resize.line{color:#1cb127}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons button{width:30px;height:30px;margin-left:4px;margin-right:4px}.DataView-Footer .Footer-Right .DataView-Share-Buttons>.Buttons button:focus{border-radius:50%;border:1px dotted #707070;outline:none}.DataView .overlay{position:absolute;display:flex;align-items:center;justify-content:center;z-index:1;top:0;left:0;width:100%;height:100%;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;opacity:.8}.DataView .overlay>.overlay-text{text-align:center;padding:2em;width:60%;background:#4d4d4d;border-radius:8px;color:#fff !important}textarea{font:400 11px system-ui;width:100%;height:2.4rem}",""]),t.exports=e},433:function(t,e,n){"use strict";var r=n(332),o=n.n(r);e.default=o.a},434:function(t,e,n){(e=n(13)(!1)).push([t.i,'.container_1VuG7{width:100%;box-sizing:border-box;color:#008830;line-height:1.35;padding-left:0 !important}.container_1VuG7 *{box-sizing:border-box}.container_1VuG7 ul{padding-left:0}.group_MrdNH{flex:0 0 auto;padding-left:3px !important;border-top:3px solid #008830;border-left:3px solid #008830}.content_TJIht{padding:5px 10px;display:flex;justify-content:space-between;align-items:center;width:100%;border:3px solid #008830}.content_TJIht>span{display:block;font-size:14px;font-size:0.875rem}.content_TJIht>span:first-child{text-align:left;margin-top:1px;flex-shrink:2}.content_TJIht>span:last-child{margin-left:10px;text-align:right;flex-shrink:1}.content_TJIht>span:not(:last-child){overflow-wrap:break-word}.content_TJIht strong{font-size:16px;font-size:1rem}.content_TJIht span.unit_1E2ZH{font-size:14px;font-size:0.875rem}.box_1NKW3{display:block;margin-top:3px}.box_1NKW3.parent_2wZWB{border-top:3px solid #008830;border-left:3px solid #008830;position:relative;padding-left:29px}.box_1NKW3.parent_2wZWB::after{content:"";display:block;position:absolute;left:-1px;bottom:0;width:30px;border-bottom:3px solid #008830}.box_1NKW3.parent_2wZWB>.content_TJIht{margin-left:-29px;width:calc(100% + 29px);border-top:none;border-left:none;border-bottom:none}@media screen and (max-width: 1263px){.group_MrdNH{padding-left:.238vw !important;border-top:.238vw solid #008830;border-left:.238vw solid #008830}.content_TJIht{padding:.396vw .792vw;border:.238vw solid #008830}.content_TJIht>span{font-size:14px;font-size:0.875rem}.content_TJIht>span:first-child{margin-top:.08vw}.content_TJIht>span:last-child{margin-left:10px}.content_TJIht strong{font-size:16px;font-size:1rem}.content_TJIht span.unit_1E2ZH{font-size:14px;font-size:0.875rem}.box_1NKW3{margin-top:.238vw}.box_1NKW3.parent_2wZWB{border-top:.238vw solid #008830;border-left:.238vw solid #008830;padding-left:2.296vw}.box_1NKW3.parent_2wZWB::after{width:2.534vw;border-bottom:.238vw solid #008830}.box_1NKW3.parent_2wZWB>.content_TJIht{margin-left:-2.296vw;width:calc(100% + 2.296vw)}}@media screen and (max-width: 959px){.group_MrdNH{padding-left:.313vw !important;border-top:.313vw solid #008830;border-left:.313vw solid #008830}.content_TJIht{padding:.521vw 1.042vw;border:.313vw solid #008830}.content_TJIht>span{font-size:14px;font-size:0.875rem}.content_TJIht>span:first-child{margin-top:.105vw}.content_TJIht>span:last-child{margin-left:10px}.content_TJIht strong{font-size:16px;font-size:1rem}.content_TJIht span.unit_1E2ZH{font-size:14px;font-size:0.875rem}.box_1NKW3{margin-top:.313vw}.box_1NKW3.parent_2wZWB{border-top:.313vw solid #008830;border-left:.313vw solid #008830;padding-left:3.02vw}.box_1NKW3.parent_2wZWB::after{width:3.334vw;border-bottom:.313vw solid #008830}.box_1NKW3.parent_2wZWB>.content_TJIht{margin-left:-3.02vw;width:calc(100% + 3.02vw)}}@media screen and (max-width: 600px){.group_MrdNH{padding-left:.5vw !important;border-top:.5vw solid #008830;border-left:.5vw solid #008830}.content_TJIht{padding:.834vw 1.667vw;border:.5vw solid #008830}.content_TJIht>span{font-size:14px;font-size:0.875rem}.content_TJIht>span:first-child{margin-top:.167vw}.content_TJIht>span:last-child{margin-left:10px}.content_TJIht strong{font-size:16px;font-size:1rem}.content_TJIht span.unit_1E2ZH{font-size:14px;font-size:0.875rem}.box_1NKW3{margin-top:.5vw}.box_1NKW3.parent_2wZWB{border-top:.5vw solid #008830;border-left:.5vw solid #008830;padding-left:4.834vw}.box_1NKW3.parent_2wZWB::after{width:5.334vw;border-bottom:.5vw solid #008830}.box_1NKW3.parent_2wZWB>.content_TJIht{margin-left:-4.834vw;width:calc(100% + 4.834vw)}}',""]),e.locals={container:"container_1VuG7",group:"group_MrdNH",content:"content_TJIht",unit:"unit_1E2ZH",box:"box_1NKW3",parent:"parent_2wZWB"},t.exports=e},435:function(t,e,n){"use strict";var r=n(333),o=n.n(r);e.default=o.a},436:function(t,e,n){(e=n(13)(!1)).push([t.i,".note_1AtEN{margin-top:10px;margin-bottom:0;font-size:12px;color:#707070}",""]),e.locals={note:"note_1AtEN"},t.exports=e},438:function(t,e,n){"use strict";var r=n(334);n.n(r).a},439:function(t,e,n){(e=n(13)(!1)).push([t.i,".DataSelector{margin-top:20px;border:1px solid #d9d9d9;background-color:#fff}.DataSelector-Button{border:none !important;margin:2px;border-radius:4px !important;height:24px !important;font-size:12px !important;color:#333 !important;background-color:#fff !important}.DataSelector-Button::before{background-color:inherit}.DataSelector-Button:focus{outline:dotted #707070 1px}.DataSelector .v-btn--active{background-color:#4d4d4d !important;color:#fff !important}",""]),t.exports=e},445:function(t,e,n){"use strict";var r=n(335);n.n(r).a},446:function(t,e,n){(e=n(13)(!1)).push([t.i,"@media screen and (min-width: 1171px){.DataView-DataInfo{text-align:right;width:50%}}.DataView-DataInfo-summary{display:inline-block;font-family:Hiragino Sans,sans-serif;font-style:normal;font-size:30px;line-height:30px}.DataView-DataInfo-summary-unit{font-size:.6em}.DataView-DataInfo-date{white-space:wrap;display:inline-block;font-size:12px;line-height:12px;color:#707070}",""]),t.exports=e},447:function(t,e,n){"use strict";var r=n(336);n.n(r).a},448:function(t,e,n){(e=n(13)(!1)).push([t.i,".OpenDataLink{text-decoration:none}.OpenDataLink .ExternalLinkIcon{vertical-align:text-bottom}",""]),t.exports=e},488:function(t,e,n){"use strict";var r=n(337);n.n(r).a},489:function(t,e,n){(e=n(13)(!1)).push([t.i,".cardTable.v-data-table{box-shadow:0 -20px 12px -12px #0003 inset}.cardTable.v-data-table th{padding:8px 10px;height:auto;border-bottom:1px solid #d9d9d9;white-space:nowrap;color:#4d4d4d;font-size:12px}.cardTable.v-data-table th.text-center{text-align:center}.cardTable.v-data-table tbody tr{color:#333}.cardTable.v-data-table tbody tr th{font-weight:normal}.cardTable.v-data-table tbody tr td{padding:8px 10px;height:auto;font-size:12px}.cardTable.v-data-table tbody tr td.text-center{text-align:center}.cardTable.v-data-table tbody tr:nth-child(odd) th,.cardTable.v-data-table tbody tr:nth-child(odd) td{background:rgba(217,217,217,.3)}.cardTable.v-data-table tbody tr:not(:last-child) td:not(.v-data-table__mobile-row){border:none}.cardTable.v-data-table:focus{outline:dotted #707070 1px}.note{padding:8px;font-size:12px;color:#707070}",""]),t.exports=e}}]);