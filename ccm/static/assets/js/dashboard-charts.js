var mss_location_check = document.getElementById("mss_location_check");
var usn_location_check = document.getElementById("usn_location_check");
var control_status_radar_this_month = document.getElementById("control_status_radar_this_month");
var control_status_radar_past_two_months = document.getElementById("control_status_radar_past_two_months");

var control_status_radar_this_month_Chart = new Chart(control_status_radar_this_month,{
    type: 'radar',
    data: {
            labels: ['Possible double selling vouchers','Abnormal Registration','Abnormal COW',
            'SIMC before activation','Registration outside location','USN Location check',
            'MSS location check','P2P transfer'],
            datasets: [{
                backgroundColor: "rgba(48, 164, 255, 0.5)",
                borderColor: "rgba(48, 164, 255, 0.8)",
                data: ['115','116', '115', '114','11','70', '115','100'],
                label: '',
                fill: false,
                showLine: false,
                pointBorderColor: "rgba(100%, 0%, 0%, 1)",
                pointBorderWidth: 2,
                pointHoverBackgroundColor: "rgb(0%, 0%, 0%)",
                pointHoverRadius: 10,
            }]
    },
    options: {
        responsive: true,
        title: {display: false,text: 'Chart'},
        legend: {position: 'top',display: false,},
        tooltips: {mode: 'index',intersect: false, enabled: true,},
        hover: {mode: 'nearest',intersect: true},
    }
});

var control_status_radar_past_two_months_Chart = new Chart(control_status_radar_past_two_months,{
    type: 'radar',
    data: {
            labels: ['Possible double selling vouchers','Abnormal Registration','Abnormal COW',
            'SIMC before activation','Registration outside location','USN Location check',
            'MSS location check','P2P transfer'],
            datasets: [{
                backgroundColor: "rgba(48, 164, 255, 0.5)",
                borderColor: "rgba(48, 164, 255, 0.8)",
                data: ['115','116', '115', '114','11','70', '115','100'],
                label: 'This Month',
                fill: true,
                showLine: false,
                pointBorderColor: "rgba(100%, 0%, 0%, 1)",
                pointBorderWidth: 2,
                pointHoverBackgroundColor: "rgb(0%, 0%, 0%)",
                pointHoverRadius: 10,
            }, {
                backgroundColor: "rgba(250, 190, 88, 1)",
                borderColor: "rgba(250, 190, 88, 1)",
                data: ['200','100', '20', '114','110','90', '115','120'],
                label: 'Past Month',
                fill: true,
                showLine: false,
                pointBorderColor: "rgba(100%, 0%, 0%, 1)",
                pointBorderWidth: 2,
                pointHoverBackgroundColor: "rgb(0%, 0%, 0%)",
                pointHoverRadius: 10,
            }],

    },
    options: {
        responsive: true,
        title: {display: false,text: 'Chart'},
        legend: {position: 'top',display: false,},
        tooltips: {mode: 'index',intersect: false, enabled: true,},
        hover: {mode: 'nearest',intersect: true},
    }
});

var MSS_Chart = new Chart(mss_location_check, {
    type: 'line',
    data: {
            labels: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','MohammadAmin'
            ,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','MohammadAmin'],
            datasets: [{
                backgroundColor: "rgba(48, 164, 255, 0.5)",
                borderColor: "rgba(48, 164, 255, 0.8)",
                data: ['1135', '1135', '1140','1168', '1150', '1145','1155', '1155', '1150','1160', '1185', '1190'
                ,'1135', '1135', '1140','1168', '1150', '1145','1155', '1155', '1150','1160', '1185', '1190'],
                label: '',
                fill: false,
                showLine: false,
                pointBorderColor: "rgba(100%, 0%, 0%, 1)",
                pointBorderWidth: 2,
                pointHoverBackgroundColor: "rgb(0%, 0%, 0%)",
                pointHoverRadius: 10,
            }]
    },
    options: {
        responsive: true,
        title: {display: false,text: 'Chart'},
        legend: {position: 'top',display: false,},
        tooltips: {mode: 'index',intersect: false, enabled: true,},
        hover: {mode: 'nearest',intersect: true},    
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: false,
                    labelString: 'Name'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Count'
                }
            }]
        }
    }
});

var USN_Chart = new Chart(usn_location_check, {
    type: 'line',
    data: {
            labels: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','MohammadAmin'
            ,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','MohammadAmin'],
            datasets: [{
                backgroundColor: "rgba(48, 164, 255, 0.5)",
                borderColor: "rgba(48, 164, 255, 0.8)",
                data: ['1135', '1135', '1140','1168', '1150', '1145','1155', '1155', '1150','1160', '1185', '1190'
                ,'1135', '1135', '1140','1168', '1150', '1145','1155', '1155', '1150','1160', '1185', '1190'],
                label: '',
                fill: false,
                showLine: false,
                pointBorderColor: "rgba(100%, 0%, 0%, 1)",
                pointBorderWidth: 2,
                pointHoverBackgroundColor: "rgb(0%, 0%, 0%)",
                pointHoverRadius: 10,
            }]
    },
    options: {
        responsive: true,
        title: {display: false,text: 'Chart'},
        legend: {position: 'top',display: false,},
        tooltips: {mode: 'index',intersect: false, enabled: true,},
        hover: {mode: 'nearest',intersect: true},    
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: false,
                    labelString: 'Name'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Count'
                }
            }]
        }
    }
});
