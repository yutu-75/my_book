/**
 * Created by ChengYa on 2016/6/18.
 */

//判断手机类型
window.onload = function () {
    //alert($(window).height());
    var u = navigator.userAgent;
    if (u.indexOf('Android') > -1 || u.indexOf('Linux') > -1) {//安卓手机
    } else if (u.indexOf('iPhone') > -1) {//苹果手机
        //屏蔽ios下上下弹性
        $(window).on('scroll.elasticity', function (e) {
            e.preventDefault();
        }).on('touchmove.elasticity', function (e) {
            e.preventDefault();
        });
    } else if (u.indexOf('Windows Phone') > -1) {//winphone手机
    }
    //预加载
    loading();
}

var date_start;
var date_end;
date_start = getNowFormatDate();


//加载页面
function loading() {
    var numbers = 0;
    var length = loading_img_url.length;

    for (var i = 0; i < length; i++) {
        var img = new Image();
        img.src = loading_img_url[i];
        img.onerror = function () {
            numbers += (1 / length) * 100;
        }
        img.onload = function () {
            numbers += (1 / length) * 100;
            $('.number').html(parseInt(numbers) + "%");
            // console.log(numbers);
            if (Math.round(numbers) == 100) {
                //$('.number').hide();
                date_end = getNowFormatDate();
                var loading_time = date_end - date_start;
                //预加载图片
                $(function progressbar() {
                    //拼接图片
                    $('.shade').hide();
                    var tagHtml = "";
                    for (var i = 0; i < length; i++) {
                        if (i == 0) {
                            // style="background:url(' + loading_img_url[i] + ') no-repeat;background-size:100% 100%;"
                            tagHtml += ' <div id="first" ><img src="' + loading_img_url[i] + '" alt="" style="width:100%;height:100%;"/></div>';
                        } else if (i == length-1) {
                            tagHtml += ' <div id="end" ><img src="' + loading_img_url[i] + '" alt="" style="width:100%;height:100%;"/></div>';
                        } else {
                            tagHtml += ' <div ><img src="' + loading_img_url[i] + '" alt="" style="width:100%;height:100%;"/></div>';
                        }
                    }
                    $(".flipbook").append(tagHtml);
                    var w = $(".graph").width();
                    $(".flipbook-viewport").show();
                });
                // 配置turn.js
                // 宽高大概按A4纸比例缩放，可自行调节
                function loadApp() {
                    // 大屏幕双页
                    if ($(window).width() > 1024 && $(window).height() > 700 ) {
                        var w = $('.flipbook-viewport').parent().width();
                        var h = $(window).height();
                        if (w == 0) { w = ((2482*2)/3368)*h; }
                        var w1 = ((2482*2)/3368)*h;
                        var h1 = (3368/(2482*2))*w;
                        if (w1 > w) {
                            h = h1;
                        } else {
                            w = w1;
                        }
                        $('.flipbook-viewport').width(w).height(h);
                        $('.flipboox').width(w).height(h);
                        $(window).resize(function () {
                            var w = $('.flipbook-viewport').parent().width();
                            var h = $(window).height();
                            if (w == 0) { w = ((2482*2)/3368)*h; }
                            var w1 = ((2482*2)/3368)*h;
                            var h1 = (3368/(2482*2))*w;
                            if (w1 > w) {
                                h = h1;
                            } else {
                                w = w1;
                            }
                            $('.flipbook-viewport').width(w).height(h);
                            $('.flipboox').width(w).height(h);
                        });

                        $('.flipbook').turn({
                            // Width
                            width: w,
                            // Height
                            height: h,
                            // Elevation
                            elevation: 50,
                            display: 'double',
                            // Enable gradients
                            gradients: true,
                            // Auto center this flipbook
                            autoCenter: true,
                            when: {
                                turning: function (e, page, view) {
                                    if (page%2 == 0) {
                                        $('.pagenumber').text(page+'-'+(page+1)+'/'+loading_img_url.length);
                                    } else {
                                        $('.pagenumber').text((page-1)+'-'+page+'/'+loading_img_url.length);
                                    }
                                    if (page == 1) {
                                        $(".btnImg").css("display", "none");
                                        $(".mark").css("display", "block");
                                        $('.pagenumber').text(page+'/'+loading_img_url.length);
                                    } else {
                                        $(".btnImg").css("display", "block");
                                        $(".mark").css("display", "none");
                                    }
                                    if (page == loading_img_url.length) {
                                        $(".nextPage").css("display", "none");
                                        $('.pagenumber').text(page+'/'+loading_img_url.length);
                                    } else {
                                        $(".nextPage").css("display", "block");
                                    }
                                },
                                turned: function (e, page, view) {
                                    // console.log(page);
                                    var total = $(".flipbook").turn("pages");//总页数
                                    if (page == 1) {
                                        $(".return").css("display", "none");
                                        $(".btnImg").css("display", "none");
                                        $('.pagenumber').text(page+'/'+loading_img_url.length);
                                    } else {
                                        $(".return").css("display", "block");
                                        $(".btnImg").css("display", "block");
                                    }
                                    if (page == 2) {
                                        $(".catalog").css("display", "block");
                                    } else {
                                        $(".catalog").css("display", "none");
                                    }
                                }
                            }
                        });
                    } else { // 小屏幕单页
                        var w = $('.flipbook-viewport').parent().width();
                        var h = $(window).height();
                        if (w == 0) { w = (2482/3368)*h; }
                        var w1 = (2482/3368)*h;
                        var h1 = (3368/2482)*w;
                        if (w1 > w) {
                            h = h1;
                        } else {
                            w = w1;
                        }
                        $('.flipbook-viewport').width(w).height(h);
                        $('.flipboox').width(w).height(h);
                        $(window).resize(function () {
                            var w = $('.flipbook-viewport').parent().width();
                            var h = $(window).height();
                            if (w == 0) { w = (2482/3368)*h; }
                            var w1 = (2482/3368)*h;
                            var h1 = (3368/2482)*w;
                            if (w1 > w) {
                                h = h1;
                            } else {
                                w = w1;
                            }
                            $('.flipbook-viewport').width(w).height(h);
                            $('.flipboox').width(w).height(h);
                        });

                        $('.flipbook').turn({
                            // Width
                            width: w,
                            // Height
                            height: h,
                            // Elevation
                            elevation: 50,
                            display: 'single',
                            // Enable gradients
                            gradients: true,
                            // Auto center this flipbook
                            autoCenter: true,
                            when: {
                                turning: function (e, page, view) {
                                    $('.pagenumber').text(page+'/'+loading_img_url.length);
                                    if (page == 1) {
                                        $(".btnImg").css("display", "none");
                                        $(".mark").css("display", "block");
                                    } else {
                                        $(".btnImg").css("display", "block");
                                        $(".mark").css("display", "none");
                                    }
                                    if (page == loading_img_url.length) {
                                        $(".nextPage").css("display", "none");
                                    } else {
                                        $(".nextPage").css("display", "block");
                                    }
                                },
                                turned: function (e, page, view) {
                                    // console.log(page);
                                    $('.pagenumber').text(page+'/'+loading_img_url.length);
                                    var total = $(".flipbook").turn("pages");//总页数
                                    if (page == 1) {
                                        $(".return").css("display", "none");
                                        $(".btnImg").css("display", "none");
                                    } else {
                                        $(".return").css("display", "block");
                                        $(".btnImg").css("display", "block");
                                    }
                                    if (page == 2) {
                                        $(".catalog").css("display", "block");
                                    } else {
                                        $(".catalog").css("display", "none");
                                    }
                                }
                            }
                        });
                    }



                    
                }
                yepnope({
                    test: Modernizr.csstransforms,
                    yep: ['/static/js/turn.js'],
                    complete: loadApp
                });
            }
            ;
        }
    }
}

function getNowFormatDate() {
    var date = new Date();
    var seperator1 = "";
    var seperator2 = "";
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    if (month >= 1 && month <= 9) {
        month = "0" + month;
    }
    if (strDate >= 0 && strDate <= 9) {
        strDate = "0" + strDate;
    }
    var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate
        + "" + date.getHours() + seperator2 + date.getMinutes()
        + seperator2 + date.getSeconds();
    return currentdate;
}


