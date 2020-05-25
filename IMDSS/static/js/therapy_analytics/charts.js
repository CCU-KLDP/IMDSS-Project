// take care of post request, by django official
function getCookie(name) {  
    var cookieValue = null;  
    if (document.cookie && document.cookie != '') {  
        var cookies = document.cookie.split(';');  
        for (var i = 0; i < cookies.length; i++) {  
            var cookie = jQuery.trim(cookies[i]);  
            // Does this cookie string begin with the name we want?  
            if (cookie.substring(0, name.length + 1) == (name + '=')) {  
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));  
                break;  
            }  
        }  
    }  
    return cookieValue;  
}  
var csrftoken = getCookie('csrftoken');  
  
function csrfSafeMethod(method) {  
    // these HTTP methods do not require CSRF protection  
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
}  
$.ajaxSetup({  
    crossDomain: false, // obviates need for sameOrigin test  
    beforeSend: function(xhr, settings) {  
        if (!csrfSafeMethod(settings.type)) {  
            xhr.setRequestHeader("X-CSRFToken", csrftoken);  
        }  
    }  
});  





// our code
function fetch_success_ratio_chart(selected_therapy) {
    for(i=0;i < selected_therapy.split("**seperator**").length;i++){    
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/therapy_analytics/success_ratio_chart",
            data: {
                "selected_dept": $("#dept_select option:selected").text(),
                "selected_disease": $("#disease_select option:selected").text(),
                "selected_therapy": selected_therapy.split("**seperator**")[i]
            },
            async:false,
            success: function (result) {
                var success_ratio_chart = echarts.init($("#success_ratio_chart_container").find(".success_ratio_chart").eq(i).get(0), 'white', {renderer: 'canvas'});
                var re_obj = (new Function("return " + result))();
                success_ratio_chart.setOption(re_obj);
            }
        });
    }
}


function fetch_cost_bar_chart(selected_therapy) {
    var cost_bar_chart = echarts.init(document.getElementById("cost_bar_chart"), 'white', {renderer: 'canvas'});
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/therapy_analytics/cost_bar_chart",
        data: {
            "selected_dept": $("#dept_select option:selected").text(),
            "selected_disease": $("#disease_select option:selected").text(),
            "selected_therapy": selected_therapy
        },
        success: function (result) {
            var re_obj = (new Function("return " + result))();
            cost_bar_chart.setOption(re_obj);   
        }
    });
    
}


function fetch_select_thread_chart(selected_therapy) {
    var thread_chart = echarts.init(document.getElementById("thread_chart"), 'white', {renderer: 'canvas'});
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/therapy_analytics/select_chart/thread_chart",
        data: {
            "selected_dept": $("#dept_select option:selected").text(),
            "selected_disease": $("#disease_select option:selected").text(),
            "selected_therapy": selected_therapy
        },
        dataType: 'json',
        success: function (result) {
            thread_chart.setOption(result.data, {'notMerge': true});
            thread_chart.on('click', function (param) {
                
                selected_therapy=""
                
                $(".therapy_checkbox_items>input:checked[name=therapy]").each(function(index){
                    if($(this)[0].checked){
                        selected_therapy+=$(this).next('span').text(); 
                        selected_therapy+=" ";
                    }
                });
            
                selected_therapy = selected_therapy.slice(0, -1)

                fetch_select_pie_chart(selected_therapy, param.name)
            }); 
        }
    });
    
}

function fetch_select_pie_chart(selected_therapy, selected_year) {
    var pie_chart = echarts.init(document.getElementById("pie_chart"), 'white', {renderer: 'canvas'});
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/therapy_analytics/select_chart/pie_chart",
        data: {
            "selected_dept": $("#dept_select option:selected").text(),
            "selected_disease": $("#disease_select option:selected").text(),
            "selected_therapy": selected_therapy,
            "selected_year": selected_year
        },
        success: function (result) {
            var re_obj = (new Function("return " + result))();
            pie_chart.setOption(re_obj, {'notMerge': true});
        }
    });    
}
