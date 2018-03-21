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
        $('#gatlingDate').html(html.join(''))
        reportList(date[0])
    })
}

function reportList(date)
{
    var url = '/report/gatling/' + date
    httpUtil.ajax(url, function(result){
        var report = result.data
        var html = [], h = -1;
        var testArray = []
        var resourceArray = []
        var loadArray = []
        for(var i = 0; i < report.length; i++)
        {
            var values = report[i].split("_");
            var testId = values[0]
            var testInfo = values[1].split("-");
            var date = testInfo[2]
            var linkUrl = url + '/' + report[i] + '/index.html'
            testArray.push(testId)
            resourceArray.push(testInfo[0])
            loadArray.push(testInfo[1])

            html[++h] = '<tr class="' + testId + ' ' + testInfo[0] + ' ' + testInfo[1] + '">';
            html[++h] = '    <td>' + testId + '</td>';
            html[++h] = '    <td>' + testInfo[0] + '</td>';
            html[++h] = '    <td>' + testInfo[1] + '</td>';
            html[++h] = '    <td>' + dateFormat(date) + '</td>';
            html[++h] = '    <td>' + linkButton(linkUrl) + '</td>';
            html[++h] = '</tr>';
        }
        $('#gatlingList').html(html.join(''))

        selectList('#testList', testArray)
        selectList('#resourceList', resourceArray)
        selectList('#loadList', loadArray)
        filterList()
    })
}

function selectList(target, array)
{
    var html = [], h = -1;
    var optionList = removeDupleArray(array)
    html[++h] = '<option value="All">All</option>';
    for(var i = 0; i < optionList.length; i++)
    {
        html[++h] = '<option value="' + optionList[i] + '">' + optionList[i] + '</option>';
    }
    $(target).html(html.join(''))
}

function filterList()
{
    var targetFilter = ".gatling-filter";
    var targetList = '#gatlingList > tr';
    var dNone = "d-none";
    var filters = []

    $(targetFilter).each(function(){
        filters.push({
            key: $(this).val(),
            className: $(this).attr("id")
        })
    })

    $(targetList).removeClass(dNone)
    for(var i = 0; i < filters.length; i++)
    {
        var key = filters[i].key;
        var className = filters[i].className;
        $(targetList).addClass(className)

        if(key == 'All')
        {
            $(targetList).removeClass(className)
        }
        else
        {
            $('.' + key).each(function(){
                $(this).removeClass(className)
            })
        }

        $('.' + className).each(function(){
            if(!$(this).hasClass(dNone))
            {
                $(this).addClass(dNone)
            }
        })
    }
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

function removeDupleArray(array)
{
    var newArray = []
    $.each(array, function(index, value){
        if($.inArray(value, newArray) === -1)
        {
            newArray.push(value);
        }
    });
    return newArray
}

$(document).ready(function() {
    reportDate();

    $('#gatlingDate').change(function(){
        reportList(this.value)
    })
    $('#testList').add('#resourceList').add('#loadList').change(function(){
        filterList()
    })
});