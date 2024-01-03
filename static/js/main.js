'use strict';

var chart = {
  height: 100,
  parentHeightOffset: 0,
  type: 'area',
  toolbar: { show: false },
  stacked: true
};

var grid = {
  borderColor: 'rgba(72,94,144, 0.07)',
  padding: {
    top: -20,
    left: -20,
    right: -20,
    bottom: 0
  },
  yaxis: {
    lines: { show: false }
  }
};

var stroke = {
  curve: 'straight',
  width: 1.5
};

var fill = {
  type: 'gradient',
  gradient: {
    opacityFrom: 0.5,
    opacityTo: 0,
  }
};

var yaxis = {
  min: 0,
  max: 80,
  show: false
}

// Math Average
var optionOne = {
  series: [{
    data: dp3 // mathAverage
  }],
  chart: chart,
  colors: ['#fd7e14'],
  grid: grid,
  stroke: stroke,
  xaxis: {
    type: 'numeric',
    tickAmount: 6,
    min: 5,
    max: 55,
    decimalsInFloat: 0,
    axisBorder: { show: false },
    labels: {
      style: {
        colors: '#6e7985',
        fontSize: '9px'
      }
    },
  },
  yaxis: yaxis,
  fill: fill,
  dataLabels: { enabled: false },
  legend: { show: false },
  tooltip: { enabled: false }
};

var chartOne = new ApexCharts(document.querySelector('#apexChart1'), optionOne);
chartOne.render();

// Reading Average
var optionTwo = {
  series: [{
    data: dp3 // readingAverage
  }],
  chart: chart,
  colors: ['#1c96e9'],
  grid: grid,
  stroke: stroke,
  xaxis: {
    type: 'numeric',
    tickAmount: 6,
    min: 45,
    max: 95,
    decimalsInFloat: 0,
    axisBorder: { show: false },
    labels: {
      style: {
        colors: '#6e7985',
        fontSize: '9px'
      }
    },
  },
  yaxis: yaxis,
  fill: fill,
  dataLabels: { enabled: false },
  legend: { show: false },
  tooltip: { enabled: false }
};

var chartTwo = new ApexCharts(document.querySelector('#apexChart2'), optionTwo);
chartTwo.render();

// Writing Average
var optionThree = {
  series: [{
    data: dp3 // writingAverage
  }],
  chart: chart,
  colors: ['#0cb785'],
  grid: grid,
  stroke: stroke,
  xaxis: {
    type: 'numeric',
    tickAmount: 6,
    min: 15,
    max: 75,
    decimalsInFloat: 0,
    axisBorder: { show: false },
    labels: {
      style: {
        colors: '#6e7985',
        fontSize: '9px'
      }
    },
  },
  yaxis: yaxis,
  fill: fill,
  dataLabels: { enabled: false },
  legend: { show: false },
  tooltip: { enabled: false }
};

var chartThree = new ApexCharts(document.querySelector('#apexChart3'), optionThree);
chartThree.render();

// Total Average
var optionFour = {
  series: [{
    data: dp3 // totalAverage
  }],
  chart: chart,
  colors: ['#506fd9'],
  grid: grid,
  stroke: stroke,
  xaxis: {
    type: 'numeric',
    tickAmount: 6,
    min: 35,
    max: 85,
    decimalsInFloat: 0,
    axisBorder: { show: false },
    labels: {
      style: {
        colors: '#6e7985',
        fontSize: '9px'
      }
    },
  },
  yaxis: yaxis,
  fill: fill,
  dataLabels: { enabled: false },
  legend: { show: false },
  tooltip: { enabled: false }
};

var chartFour = new ApexCharts(document.querySelector('#apexChart4'), optionFour);
chartFour.render();

//----------------------------------------------------

// ---------------------------------------------------------

// The Scores Distribution Bar Chart

  function fetchAndUpdateScores() {
    fetch('/get_scores_data/')
        .then(response => response.json())
        .then(data => {
            updateScoresChart(data.math_scores, data.reading_scores, data.writing_scores);
        })
        .catch(error => {
            console.error('Error fetching scores data:', error);
        });
}

  // Function to update the ApexChart with new data
  function updateScoresChart(mathScores, readingScores, writingScores) {
      var scoresChartOptions = {
          series: [{
              name: 'Math Scores',
              data: mathScores
          }, {
              name: 'Reading Scores',
              data: readingScores
          }, {
              name: 'Writing Scores',
              data: writingScores
          }],
          chart: {
              height: 290,
              parentHeightOffset: 0,
              stacked: false,
              type: 'bar',
              toolbar: { show: true }
          },
          colors: ['#fd7e14', '#1C96E9','#0CB785'],
          grid: {
              borderColor: 'rgba(72, 94, 144, .1)',
              padding: {
                  top: -20
              }
          },
          dataLabels: {
              enabled: false
          },
          stroke: {
              curve: 'straight',
              width: 1.5
          },
          xaxis: {
              type: 'numeric',
              tickAmount: 6,
              axisBorder: {
                  show: false
              },
              labels: {
                  style: {
                      colors: '#6e7985',
                      fontSize: '11px'
                  }
              }
          },
          yaxis: {
              min: 0,
              max: 140,
              tickAmount: 6,
              labels: {
                  style: {
                      colors: '#6e7985',
                      fontSize: '11px'
                  }
              }
          },
          fill: {
              type: 'color',
              gradient: {
                  opacityFrom: 0.5,
                  opacityTo: 0,
              }
          },
          legend: {
              show: true
          },
          tooltip: {
              enabled: true
          }
      };

      var scoresBarChart = new ApexCharts(document.querySelector('#scoresBarChart'), scoresChartOptions);
      scoresBarChart.render();
  }

  // Initially fetch and display scores
  document.addEventListener('DOMContentLoaded', function() {
    fetchAndUpdateScores();
});

// ---------------------------------------------------------

// Demographic Insights Charts
// Gender donut chart

//----------------------------------------------------



  // Define the gender donut chart
  var gdonut = {
      labels: ['Male', 'Female'],
      datasets: [{
          data: [],  // Default values, will be updated by AJAX call
          backgroundColor: ['#0CB785', '#1C96E9']
      }]
  };

  var optionpie = {
      maintainAspectRatio: false,
      responsive: true,
      plugins: {
          legend: {
              display: true,
          }
      },
      animation: {
          animateScale: true,
          animateRotate: true
      }
  };

  var ctx2 = document.getElementById('genderDonut');
  var myDonutChart = new Chart(ctx2, {
      type: 'doughnut',
      data: gdonut,
      options: optionpie
  });



// // New Gender Donut Chart
// var optionGenderDonut = {
//   series: [],
//   chart: {
//     type: 'donut',
//   },
//   labels: ['Male', 'Female'],
//   responsive: [{
//     breakpoint: 480,
//     options: {
//       chart: {
//         width: 200
//       },
//       legend: {
//         position: 'bottom'
//       }
//     }
//   }]
// };

// var chartGenderDonut = new ApexCharts(document.querySelector('#genderDonut'), optionGenderDonut);
// chartDonut.render();





// Function to fetch gender distribution data and update the chart
function updateGenderDonutChart() {
  fetch('/get_gender_distribution/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          // Ensure the keys match the data structure from the backend
          var malePercentage = data.male || 0;
          var femalePercentage = data.female || 0;

          myDonutChart.data.datasets[0].data = [malePercentage, femalePercentage];
          myDonutChart.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  // Fetch and update chart data
  updateGenderDonutChart();
});


// ---------------------------------------------------------

// Scores for gender male barchart
function updateGenderScoresChart() {
  fetch('/get_average_scores_by_gender/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          // Update Male Scores Bar Chart
          maleChart.data.datasets[0].data = data.male;
          maleChart.update();

          // If you have a similar chart for females, update it similarly
          femaleChart.data.datasets[0].data = data.female;
          femaleChart.update();
      })
      .catch(error => console.error('Error:', error));
}




var maleScoresBar = document.getElementById('maleBarChartScores').getContext('2d');
var maleChart = new Chart(maleScoresBar, {
  type: 'bar',
  data: {
    labels: ['Math', 'Reading', 'Writing'],
    datasets: [{
      data: [],
      backgroundColor: ['#FD7E14', '#1C96E9', '#0CB785'],
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
          font: {
            size: 11
          }
        }
      },
      y: {
        grid: {
          borderWidth: 0,
          color: '#f3f5f9'
        },
        ticks: {
          color: '#465463',
          font: {
            size: 13
          }
        }
      }
    }
  }
});


var femaleScoresBar = document.getElementById('femaleBarChartScores').getContext('2d');
var femaleChart = new Chart(femaleScoresBar, {
  type: 'bar',
  data: {
    labels: ['Math', 'Reading', 'Writing'],
    datasets: [{
      data: [],
      backgroundColor: ['#FD7E14', '#1C96E9', '#0CB785'],
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
          font: {
            size: 11
          }
        }
      },
      y: {
        grid: {
          borderWidth: 0,
          color: '#f3f5f9'
        },
        ticks: {
          color: '#465463',
          font: {
            size: 13
          }
        }
      }
    }
  }
});


document.addEventListener('DOMContentLoaded', function() {
  updateGenderScoresChart();
});

// ---------------------------------------------------------

  // Define the ethnicity donut chart
  var edonut = {
    labels: ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'],
    datasets: [{
        data: [],  
        backgroundColor: ['#ea4c89', '#fd7e14', '#506fd9', '#0cb785', '#0dcaf0'],
    }]
};

var optionpieEth = {
    maintainAspectRatio: false,
    responsive: true,
    plugins: {
        legend: {
            display: true,
        }
    },
    animation: {
        animateScale: true,
        animateRotate: true
    }
};

var ethDonut = document.getElementById('ethnicDonut');
var myEthDonutChart = new Chart(ethDonut, {
    type: 'doughnut',
    data: edonut,
    options: optionpieEth
});

function updateEthnicGroupDonutChart() {
  fetch('/get_ethnic_group_distribution/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          // Make sure to match the case of the keys
          myEthDonutChart.data.datasets[0].data = [
              data['group A'] || 0,
              data['group B'] || 0,
              data['group C'] || 0,
              data['group D'] || 0,
              data['group E'] || 0
          ];
          myEthDonutChart.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateEthnicGroupDonutChart();
});

// ---------------------------------------------------------

// Ethnic group scores bar chart
var ethnicScoresBar = document.getElementById('ethnicChartScores').getContext('2d');
var ethnicScoreChart = new Chart(ethnicScoresBar, {
  type: 'bar',
  data: {
    labels: ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'],
    datasets: [{
      data: [],
      backgroundColor: ['#ea4c89', '#fd7e14', '#506fd9', '#0cb785', '#0dcaf0'],
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
          font: {
            size: 11
          }
        }
      },
      y: {
        grid: {
          borderWidth: 0,
          color: '#f3f5f9'
        },
        ticks: {
          color: '#465463',
          font: {
            size: 13
          }
        }
      }
    }
  }
});


function updateEthnicGroupScoresChart() {
  fetch('/get_average_scores_by_ethnic_group/')  // Correct URL
      .then(response => response.json())
      .then(data => {
          ethnicScoreChart.data.datasets[0].data = [
              data['group A'] || 0,
              data['group B'] || 0,
              data['group C'] || 0,
              data['group D'] || 0,
              data['group E'] || 0
          ];
          ethnicScoreChart.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateEthnicGroupScoresChart();
});

// ---------------------------------------------------------

// Define the parental status donut chart
var pdonut = {
  labels: ['Single', 'Married', 'Widowed', 'Divorced'],
  datasets: [{
      data: [],  
      backgroundColor: ['#506fd9', '#0cb785', '#ea4c89', '#ffc107'],
  }]
};

var optionpieMar = {
  maintainAspectRatio: false,
  responsive: true,
  plugins: {
      legend: {
          display: true,
      }
  },
  animation: {
      animateScale: true,
      animateRotate: true
  }
};

var parDonut = document.getElementById('maritalDonut');
var myParDonutChart = new Chart(parDonut, {
  type: 'doughnut',
  data: pdonut,
  options: optionpieMar
});


function updateParentMaritalStatusDonutChart() {
  fetch('/get_parent_marital_status_distribution/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          myParDonutChart.data.datasets[0].data = [
              data['single'] || 0, 
              data['married'] || 0, 
              data['widowed'] || 0, 
              data['divorced'] || 0
          ];
          myParDonutChart.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateParentMaritalStatusDonutChart();
});

// ---------------------------------------------------------

// Marital status scores bar chart
var maritalScoresBar = document.getElementById('maritalChartScores').getContext('2d');
var maritalScoreChart = new Chart(maritalScoresBar, {
  type: 'bar',
  data: {
    labels: ['Single', 'Married', 'Widowed', 'Divorced'],
    datasets: [{
      data: [],
      backgroundColor: ['#506fd9', '#0cb785', '#ea4c89', '#ffc107'],
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
          font: {
            size: 11
          }
        }
      },
      y: {
        grid: {
          borderWidth: 0,
          color: '#f3f5f9'
        },
        ticks: {
          color: '#465463',
          font: {
            size: 13
          }
        }
      }
    }
  }
});


function updateMaritalStatusScoresChart() {
  fetch('/get_average_scores_by_marital_status/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          maritalScoreChart.data.datasets[0].data = [
              data['single'] || 0,
              data['married'] || 0,
              data['widowed'] || 0,
              data['divorced'] || 0
          ];
          maritalScoreChart.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateMaritalStatusScoresChart();
});


// ---------------------------------------------------------

// Parental education bar chart
var parentEducation = document.getElementById('parentEducationBarScores').getContext('2d');
var parentEdBar = new Chart(parentEducation, {
  type: 'bar',
  data: {
    labels: ['Associates Degree', 'Bachelors Degree', 'High School', 'Masters Degree', 'Some College', 'Some High School'],
    datasets: [{
      label: 'Math Scores',
      data: [], // math scores
      backgroundColor: '#FD7E14',
      barPercentage: 0.5
    }, {
      label: 'Reading Scores',
      data: [], // reading scores
      backgroundColor: '#1C96E9',
      barPercentage: 0.5
    }, {
      label: 'Writing Scores',
      data: [], // writing scores
      backgroundColor: '#0CB785',
      barPercentage: 0.5
    }]
  },
  options: {
    indexAxis: 'y',
    maintainAspectRatio: false,
    responsive: true,
    plugins: {
      legend: {
        display: true
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
          borderWidth: 0,
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


function updateParentEducationScoresChart() {
  fetch('/get_average_scores_by_parent_education/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          const mathScores = [];
          const readingScores = [];
          const writingScores = [];

          // Assuming data is an object with keys as parent education levels
          for (const level of Object.keys(data)) {
              mathScores.push(data[level].math_avg);
              readingScores.push(data[level].reading_avg);
              writingScores.push(data[level].writing_avg);
          }

          parentEdBar.data.datasets[0].data = mathScores;
          parentEdBar.data.datasets[1].data = readingScores;
          parentEdBar.data.datasets[2].data = writingScores;
          parentEdBar.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateParentEducationScoresChart();
});


// ---------------------------------------------------------

// Sports pie chart
// Pie Chart
var sportsPie = {
  series: [],
  chart: {
    width: 380,
    type: 'pie',
  },
  labels: ['Sometimes', 'Regularly', 'Never'],
  colors: ['#6610f2', '#0cb785', '#ea4c89'],
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

function updateSportsPracticeChart() {
  fetch('/get_sports_practice_distribution/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          chartSportsPie.updateSeries([data.sometimes, data.regularly, data.never]);
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateSportsPracticeChart();
});



var chartSportsPie = new ApexCharts(document.querySelector('#chartSportsPie'), sportsPie);
chartSportsPie.render();

// ---------------------------------------------------------

// Average scores per sport practice

// Parental education bar chart
var sportPracticeScores = document.getElementById('sportPracticeScores').getContext('2d');
var sportsScoresBar = new Chart(sportPracticeScores, {
  type: 'bar',
  data: {
    labels: ['Sometimes', 'Regularly', 'Never'],
    datasets: [{
      data: [], // 
      backgroundColor: ['#6610f2', '#0cb785', '#ea4c89'],
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
          borderWidth: 0,
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


function updateSportsPracticeScoresChart() {
  fetch('/get_average_scores_by_sports_practice/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          sportsScoresBar.data.datasets[0].data = [
              data['sometimes'] || 0,
              data['regularly'] || 0,
              data['never'] || 0
          ];
          sportsScoresBar.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateSportsPracticeScoresChart();
});



// ---------------------------------------------------------

// Pie Chart for weekly study hours
var studyHoursPie = {
  series: [],
  chart: {
    width: 380,
    type: 'pie',
  },
  labels: ['< 5 hours', '5-10 hours', '> 10 hours'],
  colors: ['#fd7e14', '#506fd9', '#0cb785'],
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


function updateStudyHoursChartPie() {
  fetch('/get_study_hours_distribution/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          studyHoursChartPie.updateSeries([data['< 5'], data['5 - 10'], data['> 10']]);
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateStudyHoursChartPie();
});


var studyHoursChartPie = new ApexCharts(document.querySelector('#studyHoursChartPie'), studyHoursPie);
studyHoursChartPie.render();

// ---------------------------------------------------------

// study hours bar chart
var studyHoursScoresBar = document.getElementById('studyHoursScoresBar').getContext('2d');
var studyScoresBar = new Chart(studyHoursScoresBar, {
  type: 'bar',
  data: {
    labels: ['< 5 hours', '5-10 hours', '> 10 hours'],
    datasets: [{
      data: [], // 
      backgroundColor: ['#fd7e14', '#506fd9', '#0cb785'],
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
          borderWidth: 0,
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

function updateStudyScoresBarChart() {
  fetch('/get_average_scores_by_study_hours/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          studyScoresBar.data.datasets[0].data = [
              data['< 5'] || 0,
              data['5 - 10'] || 0,
              data['> 10'] || 0
          ];
          studyScoresBar.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateStudyScoresBarChart();
});

// ---------------------------------------------------------

// Pie Chart for prep test
var testPrepPie = {
  series: [],
  chart: {
    width: 380,
    type: 'pie',
  },
  labels: ['Completed', 'None'],
  colors: ['#0cb785', '#ea4c89'], // Custom colors for the slices
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


function updateTestPrepChartPie() {
  fetch('/get_test_prep_distribution/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          testPrepPie.series = [data['completed'], data['none']];
          var chartTestPrepPie = new ApexCharts(document.querySelector('#chartTestPrepPie'), testPrepPie);
          chartTestPrepPie.render();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateTestPrepChartPie();
});

// ---------------------------------------------------------

// test prep bar chart
var testPrepScoresBar = document.getElementById('testPrepScoresBar').getContext('2d');
var testpScoresBar = new Chart(testPrepScoresBar, {
  type: 'bar',
  data: {
    labels: ['Completed', 'None'],
    datasets: [{
      data: [], // 
      backgroundColor: ['#0cb785', '#ea4c89'],
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
          borderWidth: 0,
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

function updateTestPrepScoresBarChart() {
  fetch('/get_average_scores_by_test_prep/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          testpScoresBar.data.datasets[0].data = [
              data['completed'] || 0,
              data['none'] || 0
          ];
          testpScoresBar.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateTestPrepScoresBarChart();
});


// ---------------------------------------------------------

// is firstchild bar chart
var isFirstChildScoresBar = document.getElementById('isFirstChildScoresBar').getContext('2d');
var isFCScoresBar = new Chart(isFirstChildScoresBar, {
  type: 'bar',
  data: {
    labels: ['Yes', 'No'],
    datasets: [{
      data: [], // 
      backgroundColor: '#1C96E9',
      barPercentage: 0.5,
      barThickness: 7, // Set the thickness of the bar
    }]
  },
  options: {
    indexAxis: 'y',
    maintainAspectRatio: false,
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
          borderWidth: 0,
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


function updateIsFCScoresBarChart() {
  fetch('/get_average_scores_by_first_child_status/')  // Update with the correct URL
      .then(response => response.json())
      .then(data => {
          isFCScoresBar.data.datasets[0].data = [
              data['yes'] || 0,
              data['no'] || 0
          ];
          isFCScoresBar.update();
      })
      .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  updateIsFCScoresBarChart();
});



// Dark skin integration
// function switchDark(enabled) {
//   if(enabled) {
//     chart1.options.scales['y'].grid.borderColor = '#222b41';
//     chart1.options.scales['x'].ticks.color = 'rgba(255,255,255,.65)';

//     chart2.options.scales['x'].grid.color = '#222b41';
//     chart2.options.scales['x'].ticks.color = 'rgba(255,255,255,.65)';
//     chart2.options.scales['x'].grid.borderColor = '#222b41';
//     chart2.options.scales['y'].grid.color = '#222b41';
//     chart2.options.scales['y'].ticks.color = 'rgba(255,255,255,.65)';

//     chart2.data.datasets[1].backgroundColor = '#222b41';

//     $('.btn-white').addClass('btn-outline-primary').removeClass('btn-white');

//   } else {
//     chart1.options.scales['y'].grid.borderColor = '#e2e5ec';
//     chart1.options.scales['x'].ticks.color = '#313c47';

//     chart2.options.scales['x'].grid.color = '#edeff6';
//     chart2.options.scales['x'].ticks.color = '#42484e';
//     chart2.options.scales['x'].grid.borderColor = '#edeff6';
//     chart2.options.scales['y'].grid.color = '#edeff6';
//     chart2.options.scales['y'].ticks.color = '#42484e';

//     chart2.data.datasets[1].backgroundColor = '#e2e5ec';

//     $('.btn-outline-primary').addClass('btn-white').removeClass('btn-outline-primary');
//   }

//   chart1.update();
//   chart2.update();
// }

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
