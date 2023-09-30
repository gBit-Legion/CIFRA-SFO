var ranges = [
    [13.7, 25.6],
    [13.3, 21.8],
    [11.2, 19.9],
    [7.9, 17.3],
    [4.9, 20.6],
    [5.1, 16.8],
    [9.3, 21.1],
    [11.1, 20.5],
    [8.9, 18.4],
    [4.6, 23.2],
    [11.5, 26.0],
    [8.6, 23.4],
    [9.8, 22.2],
    [8.1, 18.2],
    [5.9, 20.2],
    [4.5, 20.2],
    [8.9, 19.8],
    [11.1, 22.1],
    [7.9, 26.7],
    [15.9, 28.6],
    [14.9, 27.5],
    [9.5, 26.0],
    [11.5, 22.4],
    [8.6, 21.1],
    [12.9, 21.7],
    [13.6, 20.9],
    [9.6, 23.9],
    [8.6, 22.7],
    [7.5, 25.7],
    [5.5, 24.3],
    [10.4, 21.2]

],
averages = [
    [18.1],
    [17.1],
    [15.2],
    [12.7],
    [13.3],
    [10.6],
    [15.6],
    [16.1],
    [14.0],
    [15.3],
    [17.5],
    [17.5],
    [15.3],
    [13.9],
    [13.7],
    [13.8],
    [14.0],
    [15.8],
    [18.6],
    [21.5],
    [19.8],
    [17.6],
    [16.8],
    [15.6],
    [16.7],
    [16.3],
    [17.2],
    [16.0],
    [16.9],
    [16.1],
    [14.5]
];


Highcharts.chart('container', {

title: {
    text: 'Количество багажа',
    align: 'left'
},

subtitle: {
    text: '',
    align: 'left'
},

xAxis: {
    type: 'datetime',
    accessibility: {
        rangeDescription: ''
    }
},

yAxis: {
    title: {
        text: null
    }
},

tooltip: {
    crosshairs: true,
    shared: true,
    valueSuffix: ''
},

plotOptions: {
    series: {
        pointStart: Date.UTC(2023, 9, 31),
        pointIntervalUnit: 'day'
    }
},

series: [{
    name: '',
    data: async function requestData() {
        const result = await fetch("http://127.0.0.1:8000/cpu_count/");
        if (result.ok) {
          const data = await result.json();
          console.log(data)
          const objJson = JSON.stringify(data);
          const name = JSON.parse(objJson).cpuCount
          console.log(objJson)

          const point = [(new Date()).getTime(), name];
          const series = chart.series[0],
            shift = series.data.length > 20; // shift if the series is longer than 20

          // add the point
          chart.series[0].addPoint(point, true, shift);
        }
      },
    zIndex: 1,
    marker: {
        fillColor: 'white',
        lineWidth: 2,
        lineColor: Highcharts.getOptions().colors[0]
    }
}, {
    name: '',
    data: async function requestData() {
        const result = await fetch("http://127.0.0.1:8000/cpu_count/");
        if (result.ok) {
          const data = await result.json();
          console.log(data)
          const objJson = JSON.stringify(data);
          const name = JSON.parse(objJson).cpuCount
          console.log(objJson)

          const point = [(new Date()).getTime(), name];
          const series = chart.series[0],
            shift = series.data.length > 20; // shift if the series is longer than 20

          // add the point
          chart.series[0].addPoint(point, true, shift);
        }
      },
    type: 'arearange',
    lineWidth: 0,
    linkedTo: ':previous',
    color: Highcharts.getOptions().colors[0],
    fillOpacity: 0.3,
    zIndex: 0,
    marker: {
        enabled: false
    }
}]
});