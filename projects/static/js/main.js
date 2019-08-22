$(document).ready(function () {
    var navIcon = $("#NavbarIcon");
    var sideBar = $("#side-bar");

    navIcon.click(function () {
        sideBar.toggleClass("openNavbar");
    });

    $(document).mouseup(function (e) {
        if ( $(e.target).closest(navIcon).length === 0 ) {
            sideBar.removeClass("openNavbar");
        }
    });

    $("#contactMe").click(function () {
        console.log("asdf");
        $("#contactModal").modal("show");
    });

    $("#contactMeD").click(function () {
        console.log("asdf");
        $("#contactModal").modal("show");
    });
});