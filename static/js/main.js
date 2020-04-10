$(window).on('load', function() {
    $('.loading-wrapper').fadeOut('slow');
})
AOS.init({
    offset: 100,
    duration: 1000,
});
/* Bottom to top Button*/
b2t = document.getElementById('b2t');
window.onscroll = function() {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        b2t.style.display = "inline-block";
    } else {
        b2t.style.display = "none";
    }
}

function bottom2top() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
const hero = document.querySelector(".hero");
const slider = document.querySelector(".slider");
const logo = document.querySelector("#logo");
const ham = document.querySelector(".ham");
const headline = document.querySelector(".headline");
const showMenu = document.querySelector(".ham");
const hideMenu = document.querySelector('.closeBtn');
var hamMenu = document.querySelector('.hamMenu');

const t1 = new TimelineMax();
try {
    t1.fromTo(hero, 1, { height: "0%" }, { height: "80%", ease: Power2.easeInOut })
        .fromTo(hero, 1.2, { width: '100%' }, { width: "80%", ease: Power2.easeInOut })
        .fromTo(slider, 1.2, { x: '-100%' }, { x: "0%", ease: Power2.easeInOut }, '-=1.2')
        .fromTo(logo, 0.5, { opacity: 0, x: 30 }, { opacity: 1, x: 0, ease: Power2.easeInOut }, '-=0.5')
        .fromTo(ham, 0.5, { opacity: 0, x: 30 }, { opacity: 1, x: 0, ease: Power2.easeInOut }, '-=0.8')
        .fromTo(headline, 1, { opacity: 0, x: 0, y: 0 }, { opacity: 1, x: 0, y: -100, ease: Power2.easeInOut }, '-=0.5');
} catch (err) {
    console.log('header section is not here.Hence sppressing the error');
}

$(window).scroll(function() {
    var hT = $('#activities').offset().top,
        hH = $('#activities').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
    /*console.log(hT, hH, wH, wS);*/
    /*if (wS > (hT + hH - wH)) {}*/
});

$(hideMenu).on('click', function() {
    console.log('CloseMenu clicked');
    hamMenu.style.display = 'none';
})

$(showMenu).on('click', function() {
    console.log('ShowMenu clicked');
    hamMenu.style.display = 'flex';
})


$(document).ready(function() {
    var showChar = 120;
    var ellipsestext = "...";
    var moretext = "more";
    var lesstext = "less";
    $('.more').each(function() {
        var content = $(this).html();
        var sH = $(this)[0].scrollHeight;
        console.log(sH);

        if (content.length > showChar) {

            var c = content.substr(0, showChar);
            var h = content.substr(showChar - 1, content.length - showChar);

            var html = c + '<span class="moreellipses">' + ellipsestext + '&nbsp;</span><span class="morecontent"><span>' + h + '</span>&nbsp;&nbsp;<a href="" class="morelink">' + moretext + '</a></span>';

            $(this).html(html);
        }

    });

    $(".morelink").click(function(e) {
        if ($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            e.stopPropagation();
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });

});