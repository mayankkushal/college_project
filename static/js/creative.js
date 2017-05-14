$(function () {
    var button = $('#feedback-submit').prop('hidden', true);
    var radios = $('input[type="radio"]');
    var arr    = $.map(radios, function(el) { 
                return el.name; 
              });

    var groups = $.grep(arr, function(v, k){
            return $.inArray(v ,arr) === k;
    }).length;

    radios.on('change', function () {
        button.prop('hidden', radios.filter(':checked').length < groups);
    });

    var ctx = document.getElementById("activity-chart");
    var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Low", "Medium", "High"],
        datasets: [{
            label: 'Feedback',
            data: [low, medium, high],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 2,
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    max : total,
                    stepSize : 5,
                    beginAtZero:true
                },
                }],
            xAxes: [{ barThickness: 73,
                categoryPercentage : 1, 
            }]
            },
            maintainAspectRatio: false,
            responsive: true
    },
});
});