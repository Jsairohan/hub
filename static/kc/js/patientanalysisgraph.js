window.onload = function () {
    CanvasJS.addColorSet("allColors",
                [
                "#ff704d",//high
                "#8080ff",//moderate
                "#66ff66",//low
                "#000000" //dia 
                ]);
    CanvasJS.addColorSet("obesityColors",
                [
                "#4da6ff",//overweight
                "#00cc99",//underweight
                "#00b300",//normal
                "#ff9933",//3CB371
                "#ff6666"  //obese                
                ]);
    var chart = new CanvasJS.Chart("cardiacChart", {
	colorSet: "allColors",
        animationEnabled: true,
        // exportEnabled: true,
        title: {
            text: "Cardiac Related",
            horizontalAlign: "center",
            fontFamily:"apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif ",
            fontColor: "#64c1b1",
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            innerRadius: 100,
            indexLabelFontSize: 17,
            indexLabel: "{label}  - #percent%",
            toolTipContent: "<b>{label}:</b> {y} patients (#percent%)",
            dataPoints: [
                { y: Number(heart_high), label: "High" },
                { y: Number(heart_low), label: "Moderate" },
                { y: Number(heart_mod), label: "Low" },
                { y: Number(heart_dia), label: "Diagnosed" }
                // { y: 18, label: "High" },
                // { y: 21, label: "Moderate" },
                // { y: 1, label: "Low" },
                // { y: 6, label: "Diagnosed" }
            ]
        }]

    });
    showDefaultText(chart, "No Data Found!");
    ///
    var chart2 = new CanvasJS.Chart("diabetesChart", {
	colorSet: "allColors",
        animationEnabled: true,
        title: {
            text: "Diabetes",
            horizontalAlign: "center",
            fontFamily:"apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif ",
            fontColor: "#64c1b1",
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            innerRadius: 100,
            indexLabelFontSize: 17,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints: [
                { y: Number(diabetes_high), label: "High" },
                { y: Number(diabetes_mod), label: "Moderate" },
                { y: Number(diabetes_low), label: "Low" },
                { y: Number(diabetes_dia), label: "Diagnosed" }
                // { y: 4, label: "High" },
                // { y:23, label: "Moderate" },
                // { y: 3, label: "Low" },
                // { y: 6, label: "Diagnosed" }
            ]
        }]

    });
    showDefaultText(chart2, "No Data Found!");
    var chart3 = new CanvasJS.Chart("hypertensionChart", {
	colorSet: "allColors",
        animationEnabled: true,
        title: {
            text: "Hypertension",
            horizontalAlign: "center",
            fontFamily:"apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif ",
            fontColor: "#64c1b1",
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            innerRadius: 100,
            indexLabelFontSize: 17,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints: [
                { y: Number(hyper_high), label: "High" },
                { y: Number(hyper_mod), label: "Moderate" },
                { y: Number(hyper_low), label: "Low" },
                { y: Number(hyper_dia), label: "Diagnosed" }
            ]
        }]

    });
    showDefaultText(chart3, "No Data Found!");
    var chart4 = new CanvasJS.Chart("obesityChart", {
	colorSet: "obesityColors",
        animationEnabled: true,
        title: {
            text: "Obesity",
            horizontalAlign: "center",
            fontFamily:"apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen-Sans, Ubuntu, Cantarell, Helvetica Neue, sans-serif ",
            fontColor: "#64c1b1",
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            innerRadius: 100,
            indexLabelFontSize: 17,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints: [
                { y: Number(obesity_overweight), label: "Overweight" },
                { y: Number(obesity_underweight), label: "Underweight" },
                { y: Number(obesity_normal), label: "Normal" },
                { y: Number(obesity_preobese), label: "Pre-Obese" },
                { y: Number(obesity_obese), label: "Obese" }
            ]
        }]

    });
    showDefaultText(chart4, "No Data Found!");

    chart.render();
    chart2.render();
    chart3.render();
    chart4.render();


    function showDefaultText(chart, text) {
        var dataPoints = chart.options.data[0].dataPoints;
        var data = []
        for (var i in dataPoints) {
            alr = dataPoints[i]
            if (alr.y != 0) {
                data.push(alr.y)
            }
        }
        var isEmpty = !(data && data.length > 0);

        if (!isEmpty) {
            for (var i = 0; i < dataPoints.length; i++) {
                isEmpty = !dataPoints[i].y;
                if (!isEmpty)
                    break;
            }
        }

        if (!chart.options.subtitles)
            chart.options.subtitles = [];
        if (isEmpty)
            chart.options.subtitles.push({
                text: text,
                verticalAlign: 'center',
            });
        else
            chart.options.subtitles = [];
    }
}