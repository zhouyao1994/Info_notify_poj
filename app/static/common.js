/**
 * Created by panew on 15-6-16.
 */
$(function () {
        var index = 6;
        // 胡圆的js
        $(".get_more").click(function () {

            for (var i = index; i < index + 3; i++) { // 每次增加三条记录
                var index_id = "#" + i;
                $(index_id)[0].style.display = "block";    //设置div显示
            }
            index = index + 3;

        });
        $("#sumbit").click(function () {
            // alert("点击提交进来");
            var list = $("input");
            var listid = new Array();
            for (var i = 0, k = 0; i < list.length; i++) {
                if (list[i].checked == true) {
                    // alert("被选择"+list[i].id);
                    listid[k] = list[i].id;
                    k++;
                } else {
                    // alert("这个没有被选择")
                }
            }
            // window.location.href = "/send/name?listid=" + listid;
            $('.modal').openModal();
        });
    }
)



