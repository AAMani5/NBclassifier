document.addEventListener( 'DOMContentLoaded', function () {
    console.log("Welcome user");
}, false );

var chart1;

document.getElementById("accept").onclick = function draw (){

  var ctx1 = document.getElementById("pie-chartcanvas-1");
  var data1 = {
        labels: ["Positive", "Negative"],
        datasets: [
            {
                label: "Positive and Negative",
                data: [1, 1],
                backgroundColor: [
                    "#DEB887",
                    "#A9A9A9",
                    "#DC143C",
                    "#F4A460",
                    "#2E8B57"
                ],
                borderColor: [
                    "#CDA776",
                    "#989898",
                    "#CB252B",
                    "#E39371",
                    "#1D7A46"
                ],
                borderWidth: [1, 1, 1, 1, 1]
            }
        ]
    };
  var options = {
       title: {
           display: true,
           position: "top",
           text: "Mood in the UK",
           fontSize: 18,
           fontColor: "#111"
       },
       legend: {
           display: true,
           position: "bottom"
       }
   };

  chart1 = new Chart(ctx1, {
        type: "pie",
        data: data1,
        options: options
    });

    httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', 'http://localhost:5000/json', false);
    httpRequest.send();
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      response = JSON.parse(httpRequest.responseText)["results"];
      positives = response.filter(function(result){return result == "positive";}).length;
      negatives = response.length - positives;
      data1.datasets[0].data[0] = positives;
      data1.datasets[0].data[1] = negatives;
      console.log(positives);
      chart1.update();
    } else {
      console.log("connection error");
    }

};
