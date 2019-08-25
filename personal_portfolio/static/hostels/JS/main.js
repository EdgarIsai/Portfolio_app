$(document).ready(function () {
    var sidebar = $("#sidebar");

    $(".toggle-btn").click(function () {
            sidebar.css("transition", "0.5s");
            sidebar.toggleClass('closeSideMenu');
    });

    $(document).mouseup(function (e) {
        if (($(e.target).closest($(".toggle-btn")).length === 0 &&
            $(e.target).closest(sidebar).length === 0) ||

            $(e.target).closest(".register").length !== 0
        ){
            sidebar.removeClass('closeSideMenu');
        }
    });



    $(".register").click(function () {
        $("#registerModal").modal("show")
    });
});