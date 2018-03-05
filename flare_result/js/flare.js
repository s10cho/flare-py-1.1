var httpUtil = {
    ajax : function(url, callback)
    {
        var apiUrl = '/api' + url

        $.ajax({
            url: apiUrl,
            type: 'POST',
            dataType: 'json',
            success: function(result)
            {
                callback(result)
            },
            error: function(xhr, ajaxOptions, thrownError)
            {
                alert('ajax fail')
            }
        })
    }
}

function reportDate()
{
    httpUtil.ajax('/report/gatling', function(result){
        var date = result.data
        var html = [], h = -1;
        for(var i = 0; i < date.length; i++)
        {
            html[++h] = '<option value="' + date[i] + '">' + dateFormat(date[i]) + '</option>';
        }
        $("#gatlingDate").html(html.join(''))
        reportList(date[0])
    })
}

function reportList(date)
{
    var url = '/report/gatling/' + date
    httpUtil.ajax(url, function(result){
        var report = result.data
        var html = [], h = -1;
        for(var i = 0; i < report.length; i++)
        {
            var values = report[i].split("-");
            var test = values[0].split("_");
            var date = values[1]
            var linkUrl = url + '/' + report[i] + '/index.html'

            html[++h] = '<tr>';
            html[++h] = '    <td>' + test[0] + '</td>';
            html[++h] = '    <td>' + test[1] + '</td>';
            html[++h] = '    <td>' + dateFormat(date) + '</td>';
            html[++h] = '    <td>' + linkButton(linkUrl) + '</td>';
            html[++h] = '</tr>';
        }
        $("#gatlingList").html(html.join(''))
    })
}

function dateFormat(date)
{
    var dateLength = date.length;
    var formatDate = '';
    if(date.length >= 8)
    {
        formatDate = date.substring(0,4) + '-' + date.substring(4,6) + '-' + date.substring(6,8);
    }
    if(date.length == 14)
    {
        formatDate = formatDate + ' ' + date.substring(8,10) + ':' + date.substring(10,12) + ':' + date.substring(12,14);
    }

    return formatDate
}

function linkButton(url)
{
    var addClass = '';
    var name = '';

    if(url.indexOf('gatling') > -1)
    {
        name = 'Gatling';
        addClass = 'btn-warning'
    }

    return '<a href="' + url + '" target="_blank" class="btn btn-sm ' + addClass + '" role="button">' + name +'</a>'
}

$(document).ready(function() {
    reportDate();

    $("#gatlingDate").change(function(){
        reportList(this.value)
    })
});