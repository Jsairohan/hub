$(document).ready(function () {
  /* $("#sidetrigger").click(function(){
    $('.sidenav').sidenav();
  }); */

  $('.sidenav').sidenav();
  $(".dropdown-trigger").dropdown({hover:true}); //for account settings in navbar
  $('.modal').modal();
  $('select').formSelect();
  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: false
  });
  // move next carousel
  $('.moveNextCarousel').click(function (e) {
    console.log("next clciked");
    e.preventDefault();
    e.stopPropagation();
    $('.carousel').carousel('next');
  });

  // move prev carousel
  $('.movePrevCarousel').click(function (e) {
    console.log("prev clicked")
    e.preventDefault();
    e.stopPropagation();
    $('.carousel').carousel('prev');
  });
  /* $('.fixed-action-btn').floatingActionButton({
    direction:"top"
  }); */

  $("#brisk").click(function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("#riskfactor").offset().top
    }, 1000);
  });
  $("#bhealthindex").click(function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("#healthindex").offset().top
    }, 1000);
  });
  $("#bvitals").click(function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("#vitals").offset().top
    }, 1000);
  });

  $("#bcharts").click(function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("#activitychart").offset().top
    }, 1000);
  });
  $("#bdiet").click(function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("#diettable").offset().top
    }, 1000);
  });
  $("#bgoal").click(function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: $("#goalsandfitness").offset().top
    }, 1000);
  });

  Chart.defaults.global.legend.labels.usePointStyle = true; //for circular legends
  var ctx = $('#lineChart');
  lis =[]
  k=[]
  console.log((calories_goalneed * 35/100),calories_goalneed)
  for (var i in list_for_calburnt){
    var intcalories_goalneed= Number(calories_goalneed);
    var pert_lo =(intcalories_goalneed * 35/100)
    console.log(pert_lo,list_for_calburnt[i])
    if (list_for_calburnt[i] < pert_lo ){
//      lis.push("rgb(255, 102, 102)")
        lis.push("#ff1a1a")
    }
    else if(list_for_calburnt[i]>intcalories_goalneed ){
      console.log("Dddddd color")
//      lis.push("rgb(0, 153, 38)")
      lis.push("#5c6bc0")

    }
    else{
//      lis.push("rgb(117, 163, 163)")
        lis.push("#99cc00")
    }
    k.push(intcalories_goalneed)

  }
  console.log(lis)


  var activitydatasets =
    [
      {
        label: "Total calories burnt",
        backgroundColor:"#4d94ff",
        borderColor: "#3e95cd",
        fill: false,
        lineTension: 0.2
      }
    ]
  var chart =  new Chart(ctx, {
    type: 'bar',
    data: {
        datasets: [

          {
            label: 'Bar Dataset',
            data: list_for_calburnt ,
            backgroundColor:lis,
          },
          {
            label: 'Line Dataset',
            data: k,
//            backgroundColor:"",
            // Changes this dataset to become a line
            type: 'line'
          },
        ],
        labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    },
    options: {
      title: {
        display: true,
        position: 'bottom',
        text: 'Diet for the Current week (in Kcal)'
      },
      legend: {
        display: false,
        position: 'top',
        labels: {
          fontColor: 'red'

        }
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Week'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Calories burnt in Kcal'
          }
        }]
      }
    }
});

  //Calorie Chart
  //activity burnt bar chart
  var ctx2 = $('#lineChart2');
  var activitydatasetsbmr =
    [
    {
      data: listcalburntValues,
      label: "Total calories burnt",
      backgroundColor:"#4d94ff",
      borderColor: "#3e95cd",
      fill: false,
      lineTension: 0.2,
    }
    //  {
    //   data: [3.5, 0, 5, (4.5,8), 0, 3, 4],
    //   label: "Running",
    //   borderColor: "#8e5ea2",
    //   fill: false,
    //   lineTension: 0.2
    // }
    ]



  var chart = new Chart(ctx2, {
    type: "line",
    // type: "radar",
    data: {
       labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
      // labels: listcalburntValues ,
      datasets: activitydatasetsbmr,
    },
    options: {
      title: {
        display: true,
        position: 'bottom',
        text: 'Activities for the Current week (in Kcal)'
      },
      legend: {
        display: false,
        position: 'top',
        labels: {
          //usePointStyle:true,
          fontColor: '#333'
        }
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Week'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Calories burnt in Kcal'
          }
        }]
      }
    }
  });
  /* End of cal burnt */
  var calorieCanvas = $('#calorieChart');
  var calorieChart = new Chart(calorieCanvas, {
    type: "doughnut",
    data: {
      labels: ["Running", "Cycling", "Gym"],
      datasets: [
        {
          label: "points",
          backgroundColor: ['#f1c40f', '#e67e22', '#16a085',],
          data: [560, 400, 600]
        }
      ]
    },
    options: {
      cutoutPercentage: 20,
      animation: { animateScale: true },
      title: { display: true, text: "Calories burnt on activity (hover on the chart to see the calories burnt)", position: "bottom" },
      tooltips: {
        callbacks: {
          label: function (tooltipItem, data) {
            //get the concerned dataset
            var dataset = data.datasets[tooltipItem.datasetIndex];
            //calculate the total of this data set
            var total = dataset.data.reduce(function (previousValue, currentValue, currentIndex, array) {
              return previousValue + currentValue;
            });
            //get the current items value
            var currentValue = dataset.data[tooltipItem.index];
            //calculate the precentage based on the total and current item, also this does a rough rounding to give a whole number
            var percentage = Math.floor(((currentValue / total) * 100) + 0.5);

            return currentValue + " cal";
          }
        }
      }
    }
  });

  //Plugin to write content in the center of Doughnut charts...
  Chart.pluginService.register({
    beforeDraw: function (chart) {
      if (chart.config.options.elements.center) {
        //Get ctx from string
        var ctx = chart.chart.ctx;
        // var ctx2 = chart.chart.ctx2;
        // ctx2 = chart.chart.label
        //Get options from the center object in options
        var centerConfig = chart.config.options.elements.center;
        var fontStyle = centerConfig.fontStyle || 'Arial';
        var txt = centerConfig.text;
        var color = centerConfig.color || '#000';
        var sidePadding = centerConfig.sidePadding || 20;
        var sidePaddingCalculated = (sidePadding / 100) * (chart.innerRadius * 2)
        //Start with a base font of 40px
        ctx.font = "40px " + fontStyle;

        //Get the width of the string and also the width of the element minus 10 to give it 5px side padding
        var stringWidth = ctx.measureText(txt).width;
        var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

        // Find out how much the font can grow in width.
        var widthRatio = elementWidth / stringWidth;
        var newFontSize = Math.floor(30 * widthRatio);
        var elementHeight = (chart.innerRadius * 2);

        // Pick a new font size so it will not be larger than the height of label.
        var fontSizeToUse = Math.min(newFontSize, elementHeight);

        //Set font settings to draw it correctly.
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
        var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
        ctx.font = fontSizeToUse + "px " + fontStyle;
        ctx.fillStyle = color;

        //Draw text in center
        ctx.fillText(txt, centerX, centerY);
      }
    }
  });


  // Hypertension Progress bar
   function hypercustomValue(val) {
       if (val != 'None'){
        if ( val < 3) {
            return 'Low';
        } else if (val == 3) {
            return 'Moderate';
        } else if (val > 3 && val < 6 ) {
            return 'High';
        } else {
           return 'diagnosed'
         }
        }
        else{
            return "Data N/A"
         }
       };


  var hyperbar = $("#hypertension_chart");
  var hyperchart = new Chart(hyperbar, {
    type: "doughnut",
    data: {
      datasets: [
        {
          label: "points",
          backgroundColor: ["#00ced1", "#000000"],
          data: [hyper_points, 6 - hyper_points]
        }
      ]
    },
    options: {
      tooltips: { enabled: false },
      cutoutPercentage: 80,
      animation: { animateScale: true },
      /* title: {
        display: true,
        text: "Hypertension",
        position: "bottom",
        fontSize:22,
        fontStyle:'Arial'
      }, */
      elements: {
        center: {
          text: hypercustomValue(hyper_points),
          color: '#808080', //Default black
          fontStyle: 'Helvetica', //Default Arial
          sidePadding: 15 //Default 20 (as a percentage)
        }
      }
    }
  });

  //Diabetes chart

  function diabeticcustomValue(total_points) {
                if (total_points != 'None'){
                    if (total_points>0 && total_points < 5) {
                     return 'Low';
                    } else if (total_points == 5) {
                        return 'Moderate';
                    } else if (total_points >5 && total_points <= 10 ) {
                        return 'High';
                    }
                    else {
                        return 'Diagnosed';
                    }
                 }
                 else {
                       return "Data N/A"
                 }
               };
  var diabetesbar = $("#diabetes_chart");
  var diabeteschart = new Chart(diabetesbar, {
    type: "doughnut",
    data: {
      datasets: [
        {
          label: "points",
          backgroundColor: ["#66cdaa", "#000000"],
          data: [dia_points, 11 - dia_points]
        }
      ]
    },
    options: {
      tooltips: { enabled: false },
      cutoutPercentage: 80,
      animation: { animateScale: true },
      /* title:
      {
        display: true,
        text: "Diabetes",
        position: "bottom",
        fontSize:22,
        fontStyle:'Arial'
      }, */
      elements: {
        center: {
          text: diabeticcustomValue(dia_points),
          color: '#808080', //Default black
          fontStyle: 'Helvetica', //Default Arial
          sidePadding: 15 //Default 20 (as a percentage)
        }
      }
    }
  });

  //Cardiac Chart

  function cardiaccustomValue(val,gender) {
                    if (val != 'None'){
                       if (gender=="Male"){
                              if (val <= 5) {
                                return 'Low';
                            } else if (val >= 8 && val <= 11) {
                                return 'Moderate';
                            } else if (val >= 12 && val <=20) {
                                return 'High';
                            }
                            else if (val>20){
                            return "Diagnosed"
                            }
                        }
                       else{
                             if (val <= 13) {
                                return 'Low';
                            } else if (val >= 14 && val <= 19) {
                                return 'Moderate';
                            } else if (val >= 20 && val <28) {
                                return 'High';
                            }else if (val>=28){
                                return "Diagnosed"
                            }

                           }
                       }
                       else{
                        return "Data N/A"
                       }
                             };

 if (cardiac_result<0) {
var kin=cardiac_result
if(kin>-4 && kin<=-1){
var kin=3
}
else if(kin>-9 && kin<=-4){
var kin=1
}

if (gender== "Male"){
    var risk_data={
      datasets: [
        {
          label: "points",
          backgroundColor: ["#8080ff","#000000"],
          data: [kin,21 - kin,gender]
        }
      ]
    }
  }
  else{

  var risk_data={
      datasets: [
        {
          label: "points",
          backgroundColor: ["#bf80ff","#000000"],
          data: [kin,28 - kin,gender]
        }
      ]
    }
    }
}

else{
if (gender== "Male"){
    var risk_data={
      datasets: [
        {
          label: "points",
          backgroundColor: ["#8080ff","#000000"],
          data: [cardiac_result,21 - cardiac_result,gender]
        }
      ]
    }
  }
  else{

  var risk_data={
      datasets: [
        {
          label: "points",
          backgroundColor: ["#bf80ff","#000000"],
          data: [cardiac_result,28 - cardiac_result,gender]
        }
      ]
    }
    }
}
  var cardiacbar = $("#cardiac_chart");
  var cardiacChart = new Chart(cardiacbar, {
    type: "doughnut",
    data: risk_data,
    options: {
      tooltips: { enabled: false },
      cutoutPercentage: 80,
      animation: { animateScale: true },
      /* title:
      {
        display: true,
        text: "Cardiac Isues",
        position: "bottom",
        fontSize:22,
        fontStyle:'Arial'
      }, */
      elements: {
        center: {
          text: cardiaccustomValue(cardiac_result,gender),
          color: '#808080', //Default black
          fontStyle: 'Helvetica', //Default Arial
          sidePadding: 15 //Default 20 (as a percentage)
        }
      }
    }
  });

  //Obesity Chart
function customValue(val) {
 if (val =='Diagnosed'){
	var riskcolor=95;
        var risktext= 'Diagnosed';
        return [riskcolor,risktext]
}
 else if (ethinicty  == "Non-Asian"){
    if (val < 18.5) {
        var riskcolor=10;
        var risktext= 'Underweight';
        return [riskcolor,risktext]
    }
    if (val >= 18.5 && val <= 24.9 ) {
        var riskcolor=40;
           var risktext= 'Normal';

            return [riskcolor,risktext]
        }
    else if (val > 24.9 && val <=  29.9) {
        var riskcolor=60;
            var risktext='Overweight';

            return [riskcolor,risktext]
        }
    else if (val > 29.9) {
        var riskcolor=80;
            var risktext='Obese';
            return [riskcolor,risktext]

        }
        }
else {
    if (val < 18.5) {
        var riskcolor=10;
        var risktext= 'Underweight';
        return [riskcolor,risktext]
    }
    else if (val >= 18.5 && val <= 22.9 ) {
        var riskcolor=40;
           var risktext= 'Normal';

            return [riskcolor,risktext]
     }
     else if (val > 22.9 && val <=  24.9) {
    var riskcolor=60;
        var risktext='Overweight';

        return [riskcolor,risktext]
    }
    else if (val > 24.9 && val <=  29.9) {
        var riskcolor=80;
            var risktext='Pre-Obese';
            return [riskcolor,risktext]
        }
    else if (val > 29.9) {
        var riskcolor=90;
            var risktext='Obese';
            return [riskcolor,risktext]
        }
	}

                                
								}
;
var obesitybar = $("#obesity_chart");
  var obesityChart = new Chart(obesitybar, {
    type: "doughnut",
    data: {
      datasets: [
        {
          label: "points",
          backgroundColor: ["#90ee90", "#000000"],
          data: [customValue(obestiy_points)[0], 100 - customValue(obestiy_points)[0]]
        }

      ]
    },
    options: {
      tooltips: { enabled: false },
      cutoutPercentage: 80,
      animation: { animateScale: true },
      /* title:
      {
        display: true,
        text: "Obesity",
        position: "bottom",
        fontSize:22,
        fontStyle:'Arial'
      }, */
      elements: {
        center: {
          text: customValue(obestiy_points)[1],
          color: '#808080', //Default black
          fontStyle: 'Helvetica', //Default Arial
          sidePadding: 15 //Default 20 (as a percentage)
        }
      }
    }
  });

  //Health Index Chart
  var HIChart = $("#healthIndexChart");
  var HIDataSets =
    [{
      data: nsysto,
      label: "Systolic",
      borderColor: "#3e95cd",
      fill: false,
      lineTension: 0.2,
      //showLine:false
    }, {
      data: ndiasto,
      label: "Diastolic",
      borderColor: "rgb(185, 212, 9)",
      fill: false,
      lineTension: 0.2,
      //showLine:false
    },
    {
      data: ngluc,
      label: "Glucose (mg/dL)",
      borderColor: "#1cd8d2",
      fill: false,
      lineTension: 0.2,
      //showLine:false
    },
    {
      data: nhdl,
      label: "HDL Cholestrol (mg/dL)",
      borderColor: "#f05b4f",
      fill: false,
      lineTension: 0.2,
      //showLine:false
    }, {
      data: ntc,
      label: "Total Cholestrol (mg/dL)",
      borderColor: "#b687ca",
      fill: false,
      lineTension: 0.2,
      //showLine:false
    }
    ]

  var chart = new Chart(HIChart, {
    type: "line",
    data: {
      labels: ndate,
      datasets: HIDataSets,
    },
    options: {
      title: {
        display: true,
        position: 'bottom',
        text: 'Health Index Report'
      },
      legend: {
        display: true,
        position: 'top',
        labels: {
          //usePointStyle:true,
          fontColor: '#333'
        }
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Date'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: ''
          }
        }]
      }
    }
  });
});