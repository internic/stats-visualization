// use strict
"use strict";

// Sessions By Location
$('#vmap').vectorMap({
    map: 'kg_en',
    backgroundColor: '#fff',
    borderColor: '#fff',
    color: '#d9dde7',
    colors: {
      'bk': '#1c96e9',
      'cy': '#fd7e14',
      'ik': '#0cb785',
      'nr': '#6984de',
      'bt': '#dc3545',
      'ja': '#0dcaf0',
      'ts': '#ffc107',
      'os': '#ffc107'
    },
    hoverColor: null,
    hoverOpacity: 0.8,
    enableZoom: true,
    showTooltip: true,
    multiSelectRegion: false
  });

// Donut charts for distributions by Gender, Ethnicity, and Marital Status

  // Donut Chart for Gender distribution
  var genderDataElement = document.getElementById('genderDonut');
  var genderData = JSON.parse(genderDataElement.getAttribute('data-gender-data'));

  var genderDonut = {
    series: genderData,
    chart: {
      type: 'donut',
    },
    labels: ['Male', 'Female'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

var chartGenderDonut = new ApexCharts(document.querySelector('#genderDonut'), genderDonut);
chartGenderDonut.render();


  // Donut Chart for Ethnicity distribution
  var ethnicityDataElement = document.getElementById('ethnicityDonut');
  var ethnicityData = JSON.parse(ethnicityDataElement.getAttribute('data-ethnicity-data'));

  var ethnicityDonut = {
    series: ethnicityData,
    chart: {
      type: 'donut',
    },
    labels: ['Kyrgyz', 'Uzbek', 'Russian', 'Dungan', 'Uigur', 'Tajik', 'Kazakh', 'Other'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

var chartEthnicityDonut = new ApexCharts(document.querySelector('#ethnicityDonut'), ethnicityDonut);
chartEthnicityDonut.render();


  // Donut Chart for Marital status distribution
  var maritalDataElement = document.getElementById('maritalDonut');
  var maritalData = JSON.parse(maritalDataElement.getAttribute('data-marital-data'));

  var maritalDonut = {
    series: maritalData,
    chart: {
      type: 'donut',
    },
    labels: ['Married', 'Divorced', 'Lives together', 'Separated', 'Widowed', 'Single'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

var chartMaritalDonut = new ApexCharts(document.querySelector('#maritalDonut'), maritalDonut);
chartMaritalDonut.render();


// Child education 

  // Pie Chart for Distribution of children by enrollment in educational institutions
  var enrollmentDataElement = document.getElementById('enrollmentChartPie');
  var enrollmentData = JSON.parse(enrollmentDataElement.getAttribute('data-enrollment-data'));

  var enrollmentPie = {
    series: enrollmentData,
    chart: {
      width: 380,
      type: 'pie',
    },
    labels: ['Enrolled', 'Not enrolled'],
    // colors: ['#fd7e14', '#506fd9', '#0cb785'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var enrollmentChartPie = new ApexCharts(document.querySelector('#enrollmentChartPie'), enrollmentPie);
  enrollmentChartPie.render();



  // Children unenrollment reasons bar chart
  var unenrollmentReasonsElement = document.getElementById('unenrollmentReasons');
  var unenrollmentReasonsData = JSON.parse(unenrollmentReasonsElement.getAttribute('data-unenrollment-reasons'));

  var unenrollmentReasons = document.getElementById('unenrollmentReasons').getContext('2d');
  var sportsScoresBar = new Chart(unenrollmentReasons, {
    type: 'bar',
    data: {
      labels: ['Costs Too Much', 'Illness', 'Does not Like Studying', 'Works to Support Family', 'Will Start School in 1-2 Years', 'Finished', 'Political Unrest', 'Other Reasons'],

      datasets: [{
        data: unenrollmentReasonsData, // 
        backgroundColor: ['#506fd9'],
        barPercentage: 0.5,
        barThickness: 7,
      }]
    },
    options: {
      indexAxis: 'y',
      maintainAspectRatio: true,
      responsive: true,
      plugins: {
        legend: {
          display: false
        }
      },
      scales: {
        x: {
          beginAtZero:true,
          max: 100,
          grid: {
            borderColor: '#e2e5ec',
            color: '#f3f5f9'
          },
          ticks: {
            color: '#212830',
            font: {
              size: 10,
              weight: '500'
            }
          }
        },
        y: {
          grid: {
            borderWidth: 1,
            color: '#f3f5f9'
          },
          ticks: {
            color: '#212830',
            font: {
              size: 12
            }
          }
        }
      }
    }
  });

  // Children spoken languages pie chart
  var languagesChartDataElement = document.getElementById('languagesChartPie');
  var languagesData = JSON.parse(languagesChartDataElement.getAttribute('data-languages-data'));

  var languagesPie = {
    series: languagesData,
    chart: {
      width: 380,
      type: 'pie',
    },
    labels: ['Kyrgyz', 'Uzbek', 'Russian', 'English', 'Turkish', 'German', 'Chinese', 'Others'],
    // colors: ['#fd7e14', '#506fd9', '#0cb785'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var languagesChartPie = new ApexCharts(document.querySelector('#languagesChartPie'), languagesPie);
  languagesChartPie.render();




  // Children expenditure dummy graph (for styling purposes)
  var dp1 = [
    [0,53],
    [1,50],
    [2,49],
    [3,47],
    [4,49],
    [5,50],
    [6,48],
    [7,48],
    [8,53],
    [9,52],
    [10,49],
    [11,50],
    [12,48],
    [13,44],
    [14,40],
    [15,41],
    [16,45],
    [17,44],
    [18,41],
    [19,38],
    [20,39],
    [21,41],
    [22,39],
    [23,35],
    [24,38],
    [25,38],
    [26,40],
    [27,38],
    [28,42],
    [29,46],
    [30,43],
    [31,40],
    [32,36],
    [33,31],
    [34,28],
    [35,29],
    [36,29],
    [37,33],
    [38,37],
    [39,35],
    [40,37],
    [41,39],
    [42,39],
    [43,34],
    [44,37],
    [45,39],
    [46,38],
    [47,37],
    [48,40],
    [49,35],
    [50,31],
    [51,31],
    [52,30],
    [53,25],
    [54,28],
    [55,28],
    [56,30],
    [57,32],
    [58,32],
    [59,37],
    [60,35],
    [61,39],
    [62,41],
    [63,41],
    [64,43],
    [65,39],
    [66,39],
    [67,43],
    [68,42],
    [69,43],
    [70,38],
    [71,43],
    [72,41],
    [73,44],
    [74,46],
    [75,47],
    [76,49],
    [77,46],
    [78,51],
    [79,50],
    [80,53],
    [81,56],
    [82,52],
    [83,56],
    [84,60],
    [85,58],
    [86,56],
    [87,55],
    [88,54],
    [89,54],
    [90,58],
    [91,57],
    [92,60],
    [93,54],
    [94,56],
    [95,55],
    [96,54],
    [97,52],
    [98,54],
    [99,54],
    [100,51],
    [101,51],
    [102,46],
    [103,48]
  ];
  
  var dp2 = [
    [0,56],
    [1,54],
    [2,59],
    [3,61],
    [4,65],
    [5,70],
    [6,73],
    [7,70],
    [8,73],
    [9,69],
    [10,73],
    [11,69],
    [12,73],
    [13,77],
    [14,72],
    [15,75],
    [16,71],
    [17,69],
    [18,67],
    [19,68],
    [20,67],
    [21,66],
    [22,61],
    [23,58],
    [24,56],
    [25,53],
    [26,52],
    [27,57],
    [28,59],
    [29,63],
    [30,60],
    [31,62],
    [32,64],
    [33,67],
    [34,66],
    [35,67],
    [36,71],
    [37,66],
    [38,64],
    [39,62],
    [40,66],
    [41,65],
    [42,62],
    [43,66],
    [44,63],
    [45,66],
    [46,64],
    [47,65],
    [48,69],
    [49,65],
    [50,69],
    [51,65],
    [52,68],
    [53,73],
    [54,71],
    [55,71],
    [56,75],
    [57,77],
    [58,81],
    [59,79],
    [60,76],
    [61,74],
    [62,75],
    [63,76],
    [64,78],
    [65,81],
    [66,82],
    [67,87],
    [68,85],
    [69,82],
    [70,82],
    [71,77],
    [72,80],
    [73,84],
    [74,83],
    [75,88],
    [76,89],
    [77,88],
    [78,83],
    [79,87],
    [80,85],
    [81,85],
    [82,90],
    [83,92],
    [84,97],
    [85,80],
    [86,82],
    [87,81],
    [88,84],
    [89,85],
    [90,90],
    [91,91],
    [92,90],
    [93,89],
    [94,86],
    [95,83],
    [96,82],
    [97,87],
    [98,85],
    [99,87],
    [100,82],
    [101,87],
    [102,86],
    [103,83]
  ];


  var optionSix = {
    series: [{
      name: 'series1',
      data: dp2
    },{
      name: 'series2',
      data: dp1
    },],
    chart: {
      height: 195,
      parentHeightOffset: 0,
      type: 'area',
      toolbar: { show: false },
      sparkline: { enabled: true }
    },
    colors: ['#85b6ff', '#506fd9'],
    grid: {
      borderColor: 'rgba(72, 94, 144, .1)',
      padding: {
        top: -20,
        left: 0
      },
      yaxis: {
        lines: { show: false }
      }
    },
    dataLabels: { enabled: false },
    stroke: {
      curve: 'straight',
      width: 1.5
    },
    xaxis: {
      type: 'numeric',
      min: 5,
      max: 90,
      tickAmount: 6,
      axisBorder: { show: false },
      labels: {
        style: {
          colors: '#6e7985',
          fontSize: '11px'
        }
      }
    },
    yaxis: {
      max: 180
    },
    fill: {
      type: 'gradient',
      gradient: {
        opacityFrom: 0.5,
        opacityTo: 0,
      }
    },
    legend: { show: false },
    tooltip: { enabled: false }
  };
  
  var chartSix = new ApexCharts(document.querySelector('#apexChart6'), optionSix);
  chartSix.render();




// Child health 0-17 y.o donut charts

  // disablity donut chart
  var disabilityChartDataElement = document.getElementById('disabilityDonut');
  var disabilityData = JSON.parse(disabilityChartDataElement.getAttribute('data-disability-data'));

  var disabilityDonut = {
    series: disabilityData,
    chart: {
      type: 'donut',
      width: '320px',
    },
    labels: ['Yes', 'No'],
    colors: ['#33d685', '#008ffb'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var chartDisabilityDonut = new ApexCharts(document.querySelector('#disabilityDonut'), disabilityDonut);
  chartDisabilityDonut.render();


  // having birth certificate donut chart
  var certificateChartDataElement = document.getElementById('certificateDonut');
  var certificateData = JSON.parse(certificateChartDataElement.getAttribute('data-certificate-data'));

  var certificateDonut = {
    series: certificateData,
    chart: {
      type: 'donut',
      width: '320px',
    },
    labels: ['Yes', 'No'],
    colors: ['#33d685', '#008ffb'],
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200
        },
        legend: {
          position: 'bottom'
        }
      }
    }]
  };

  var chartCertificateDonut = new ApexCharts(document.querySelector('#certificateDonut'), certificateDonut);
  chartCertificateDonut.render();







  // Dark skin integration
function switchDark(enabled) {

  if(enabled) {
    $('#vmap').vectorMap('set', 'backgroundColor', '#192030');

  } else {
    $('#vmap').vectorMap('set', 'backgroundColor', '#fff');
  }
}

if(skinMode) { switchDark(true); }

// Switch between light and dark
$('#skinMode .nav-link').bind('click', function(e){
  var mode = $(this).text().toLowerCase();
  if(mode == 'dark') {
    switchDark(true);
  } else {
    switchDark(false);
  }
});