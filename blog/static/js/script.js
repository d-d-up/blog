$(document).ready(function() {
    $("#nav_b").click(function() {
        if ($(this).hasClass("closed_nav_b")) {
            $(this).removeClass("closed_nav_b");
            $(this).next("ul").stop(true, true).fadeOut("200")
        } else {
            $(this).addClass("closed_nav_b");
            $(this).next("ul").stop(true, true).fadeIn("200")
        }
    });
    $(window).scroll(function() {
        $(".fixed_mok").css({
            width: $(".sidbar").width() + "px",
            left: $(".sidbar").offset().left + "px",
            top: "20px"
        });
        if ($(window).scrollTop() >= $(".sidbar").offset().top + $(".sidbar").height()) {
            $(".fixed_mok").addClass("fix_now")
        } else {
            $(".fixed_mok").removeClass("fix_now")
        }
    });
});
