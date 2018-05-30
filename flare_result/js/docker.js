var chartList = []

function dataSet()
{
    chartList = [
        {
            info: {
                canvasId: 'cpu-canvas',
                title: 'Docker CPU',
                yAxesId: 'y-axis-1',
                ticks: {max: 100, min: 0}
            },
            data:  {
                labels: data.time,
                datasets: [{
                    label: 'CPU (%)',
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgb(255, 99, 132)',
                    fill: true,
                    data: data.cpu,
                    yAxisID: 'y-axis-1',
                    radius: 0,
                }]
            }
        },
        {
            info: {
                    canvasId: 'mem-canvas',
                    title: 'Docker Memory',
                    yAxesId: 'y-axis-2',
                    ticks: {max: data.memory_size, min: 0}
                },
            data:      {
                labels: data.time,
                datasets: [{
                    label: 'Memory (GB)',
                    borderColor: 'rgb(54, 162, 235)',
                    backgroundColor: 'rgb(54, 162, 235)',
                    fill: true,
                    data: data.mem,
                    yAxisID: 'y-axis-2',
                    radius: 0,
                }]
            }
        },
    ]
}

function getParam(name)
{
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function loadData(url, callback)
{
    if(checkUrl(url))
    {
        var head = document.getElementsByTagName('head')[0];
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = url;
        script.onreadystatechange = callback;
        script.onload = callback;
        head.appendChild(script);
    }
    else
    {
        document.getElementsByClassName("container")[0].innerHTML += '<div class="alert alert-dark text-center" role="alert">No Data</div>'
    }
}

function checkUrl(url)
{
    var request = false;
    if (window.XMLHttpRequest)
    {
        request = new XMLHttpRequest;
    }
    else if (window.ActiveXObject)
    {
        request = new ActiveXObject("Microsoft.XMLHttp");
    }

    if (request)
    {
        request.open("HEAD", url, false);
        request.send();
        console.log(request.status)
        if (request.status == 0) { return true; }
    }
    return false;
}

window.onload = function() {
    var date = getParam("date");
    var testId = getParam("testId");
    var url = '/report/gatling/' + date + '/' + testId + '/dockerData.js';

    loadData(url, function(){
        dataSet();

        for(var i = 0; i < chartList.length; i++)
        {
            var chartData = chartList[i]
            var chartInfo = chartData.info
            var ctx = document.getElementById(chartInfo.canvasId).getContext('2d')
            Chart.Line(ctx, {
                data: chartData.data,
                options: {
                    responsive: true,
                    hoverMode: 'index',
                    stacked: false,
                    title: {
                        display: true,
                        text: chartInfo.title
                    },
                    scales: {
                        yAxes: [{
                            type: 'linear', // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                            display: true,
                            position: 'left',
                            id: chartInfo.yAxesId,
                            ticks : chartInfo.ticks
                        }],
                    }
                }
            });
        }
    })
};