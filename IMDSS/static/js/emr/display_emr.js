document.write('<script src="{% static "js/emr/sidenav.js" %}"</script>');

function search_icon_to_green() {
    var icon = document.getElementById("search-icon")
    var bar = document.getElementById("search-bar")
    icon.src = green_pic
    bar.style.border = "1px solid #009688"
}

function search_icon_to_black() {
    var icon = document.getElementById("search-icon")
    var bar = document.getElementById("search-bar")
    icon.src = black_pic
    bar.style.border = "1px solid black"
}

$("#select-emr-table>tbody").on("click", "tr", function() {
    var selected_emr_type = $(this).find("td:eq(3)").text();
    var url = location.href
    var selected_emr_id = $(this).attr("id")

    $("#select-emr-table>tbody>tr").removeClass("selected")
    $(this).addClass("selected")

    $.ajax({
        type: "GET",
        url: url + "get_emr",
        data: {"selected_emr_id": selected_emr_id, "selected_emr_type": selected_emr_type},
        dataType: "json",
        success: function(result){
            insert_html = result['insert_html']
            $("#emr").empty()
            $("#emr").append(insert_html)
            for(i=0;i < Object.keys(mark_dic).length;i++){
                if (Object.keys(mark_dic)[i] == selected_emr_id) {
                   for(j=0;j < Object.values(mark_dic)[i].length;j++){
                        var highlight_text = Object.values(mark_dic)[i][j].slice(0, -1)
                        var lower_highlight_text = Object.values(mark_dic)[i][j].slice(0, -1).toLowerCase();

                        var original_text = $("#emr>:contains(" + highlight_text + ")").text()
                        var lower_original_text = $("#emr>:contains(" + lower_highlight_text + ")").text()
                        
                        var new_text = original_text.replace(highlight_text, '<span style="color: red;">' + highlight_text + '</span>')
                        var lower_new_text = lower_original_text.replace(lower_highlight_text, '<span style="color: red;">' + lower_highlight_text + '</span>')
                        
                        alert(lower_highlight_text)

                        $("#emr>:contains(" + highlight_text + ")").html(new_text)
                        $("#emr>:contains(" + lower_highlight_text + ")").html(lower_new_text)
                    }
                }
            
            }
        }
        
    });
});

$("#select-emr-table tbody").on("hover", "tr", function() {
    $(this).style.bgColor=rgb(189, 189, 189)
});

$("#search-icon").on("click", function(){
    var input_text = $("input[name='input'] ").val()
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/emr_search/text_search_emr",
        data: {"input_text": input_text},
        dataType: "json",
        success: function(result){
            var html = '<i class="material-icons">search</i>'
            for(i = 0;i < $("#select-emr-table tbody tr").size();i++){
                location = '#select-emr-table tbody tr:eq(' + i + ') td:nth-child(2)'
                $(location).empty()
            }
            for(i = 0;i < result.length;i++){
                var location = '#select-emr-table tbody tr:eq(' + result[i] + ') td:nth-child(2)'
                $(location).append(html)
            }
        } 
    });
});

