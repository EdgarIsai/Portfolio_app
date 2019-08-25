$(document).ready(function () {
    if ($('.hostel-cards').length === 0) {
        $('.details').css('display', 'block', 'important');
    } else {
        var mainContent = $('.main-content');

        mainContent.css({
            'background': 'none',
            'margin':'0 auto 0',
            'margin-top': '0'
        });
    }
});