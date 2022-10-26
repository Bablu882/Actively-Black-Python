$(document).ready(function () {
  $('.toggle-button').on('click', function(){
    $('.drawer').toggle();
    $('.main-content').toggleClass('main-section')
  })
  
  //Counter
  $(".counter").each(function () {
    $(this)
      .prop("Counter", 0)
      .animate(
        {
          Counter: $(this).text(),
        },
        {
          duration: 4000,
          easing: "swing",
          step: function (now) {
            $(this).text(Math.ceil(now));
          },
        }
      );
  });
  // Color picker sidebar
  $(".color-picker-btn").on("click", function (e) {
    $(".color-picker").addClass("open-sidenav");
    $(".overlay").addClass("show-overlay");
  });
  $(".overlay").on("click", function (e) {
    $(".color-picker").removeClass("open-sidenav");
    $(this).removeClass("show-overlay");
  });
  // Change theme color
  var theme_classes =
    "dark-theme light-theme warning-theme primary-theme danger-theme success-theme info-theme navbar-light navbar-dark bg-dark bg-light bg-transparent bg-primary";
  $(".dark-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".navbar").removeClass(theme_classes);
    $(".dashboard").addClass("dark-theme");
    $(".header-common").addClass("bg-transparent");
    $(".navbar").addClass("navbar-dark");
    $(this).addClass("selected");
  });
  $(".light-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".navbar").removeClass(theme_classes);
    $(".dashboard").addClass("light-theme");
    $(".header-common").addClass("bg-primary");
    $(".navbar").addClass("navbar-light");
    $(this).addClass("selected");
  });
  $(".default-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".dashboard").addClass("default-theme");
    $(".header-common").addClass("bg-primary");
    $(this).addClass("selected");
  });
  $(".primary-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".dashboard").addClass("primary-theme");
    $(".header-common").addClass("bg-primary");
    $(this).addClass("selected");
  });
  $(".warning-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".dashboard").addClass("warning-theme");
    $(".header-common").addClass("bg-warning");
    $(this).addClass("selected");
  });
  $(".success-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".dashboard").addClass("success-theme");
    $(".header-common").addClass("bg-success");
    $(this).addClass("selected");
  });
  $(".indigo-picker").on("click", function () {
    $(".dashboard").removeClass(theme_classes);
    $(".header-common").removeClass(theme_classes);
    $(".dashboard").addClass("indigo-theme");
    $(this).addClass("selected");
  });
  // Bar graph
  // var ctx = $("#chart-line");
  // var myLineChart = new Chart(ctx, {
  //   type: "bar",
  //   data: {
  //     labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
  //     datasets: [
  //       {
  //         data: [0, 10, 20, 14, 30, 50, 18, 60, 3, 10, 7, 12],
  //         label: "Sales",
  //         borderColor: "rgb(44, 85, 149)",
  //         fill: true,
  //         backgroundColor: "rgb(44, 85, 149)",
  //       },
  //       {
  //         data: [12, 7, 10, 2, 10, 12, 14, 4, 20, 50, 40, 30],
  //         label: "Revenue",
  //         borderColor: "rgb(238 238 238)",
  //         fill: false,
  //         backgroundColor: "rgb(238 238 238)",
  //       },
  //     ],
  //   },
  //   options: {
  //     title: {
  //       display: false,
  //       //text: "Sales / Revenue",
  //     },
  //   },
  // });
 // pie
  const mdx = document.getElementById('myChart').getContext('2d');
  const myChart = new Chart(mdx, {
      type: 'doughnut',
      data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', ],
          datasets: [{
              label: '# of Votes',
              data: [12, 19, 3, 5],
              backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          },
          legend: {
            display: false
          },
          cutoutPercentage: 90,
      }
  });

  var productDetails = function () {
    $('.product-image-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: false,
        asNavFor: '.slider-nav-thumbnails',
    });

    $('.slider-nav-thumbnails').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.product-image-slider',
        dots: false,
        focusOnSelect: true,

        prevArrow: '<button type="button" class="slick-prev"><i class="fi-rs-arrow-small-left"></i></button>',
        nextArrow: '<button type="button" class="slick-next"><i class="fi-rs-arrow-small-right"></i></button>'
    });

    // Remove active class from all thumbnail slides
    $('.slider-nav-thumbnails .slick-slide').removeClass('slick-active');

    // Set active class to first thumbnail slides
    $('.slider-nav-thumbnails .slick-slide').eq(0).addClass('slick-active');

    // On before slide change match active thumbnail to current slide
    $('.product-image-slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
        var mySlideNumber = nextSlide;
        $('.slider-nav-thumbnails .slick-slide').removeClass('slick-active');
        $('.slider-nav-thumbnails .slick-slide').eq(mySlideNumber).addClass('slick-active');
    });

    $('.product-image-slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
        var img = $(slick.$slides[nextSlide]).find("img");
        $('.zoomWindowContainer,.zoomContainer').remove();
        $(img).elevateZoom({
            zoomType: "inner",
            cursor: "crosshair",
            zoomWindowFadeIn: 500,
            zoomWindowFadeOut: 750
        });
    });
    //Elevate Zoom
    if ($(".product-image-slider").length) {
        $('.product-image-slider .slick-active img').elevateZoom({
            zoomType: "inner",
            cursor: "crosshair",
            zoomWindowFadeIn: 500,
            zoomWindowFadeOut: 750
        });
    }
    //Filter color/Size
    $('.list-filter').each(function () {
        $(this).find('a').on('click', function (event) {
            event.preventDefault();
            $(this).parent().siblings().removeClass('active');
            $(this).parent().toggleClass('active');
            $(this).parents('.attr-detail').find('.current-size').text($(this).text());
            $(this).parents('.attr-detail').find('.current-color').text($(this).attr('data-color'));
        });
    });
    //Qty Up-Down
    $('.detail-qty').each(function () {
        var qtyval = parseInt($(this).find('.qty-val').text(), 10);

        var qtyInput = document.getElementById("qty-input")
        if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

        $('.qty-up').on('click', function (event) {
            event.preventDefault();
            qtyval = qtyval + 1;
            $(this).prev().text(qtyval);
            if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

        });
        $('.qty-down').on('click', function (event) {
            event.preventDefault();
            qtyval = qtyval - 1;
            if (qtyval > 1) {
                $(this).next().text(qtyval);
                if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

            } else {
                qtyval = 1;
                $(this).next().text(qtyval);
                if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

            }
        });
    });

    $('.dropdown-menu .cart_list').on('click', function (event) {
        event.stopPropagation();
    });
};

productDetails();


/*Product Details*/
var productDetails = function () {
        $('.product-image-slider').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: false,
            fade: false,
            asNavFor: '.slider-nav-thumbnails',
        });

        $('.slider-nav-thumbnails').slick({
            slidesToShow: 4,
            slidesToScroll: 1,
            asNavFor: '.product-image-slider',
            dots: false,
            focusOnSelect: true,

            prevArrow: '<button type="button" class="slick-prev"><i class="fi-rs-arrow-small-left"></i></button>',
            nextArrow: '<button type="button" class="slick-next"><i class="fi-rs-arrow-small-right"></i></button>'
        });

        // Remove active class from all thumbnail slides
        $('.slider-nav-thumbnails .slick-slide').removeClass('slick-active');

        // Set active class to first thumbnail slides
        $('.slider-nav-thumbnails .slick-slide').eq(0).addClass('slick-active');

        // On before slide change match active thumbnail to current slide
        $('.product-image-slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
            var mySlideNumber = nextSlide;
            $('.slider-nav-thumbnails .slick-slide').removeClass('slick-active');
            $('.slider-nav-thumbnails .slick-slide').eq(mySlideNumber).addClass('slick-active');
        });

        $('.product-image-slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
            var img = $(slick.$slides[nextSlide]).find("img");
            $('.zoomWindowContainer,.zoomContainer').remove();
            $(img).elevateZoom({
                zoomType: "inner",
                cursor: "crosshair",
                zoomWindowFadeIn: 500,
                zoomWindowFadeOut: 750
            });
        });
        //Elevate Zoom
        if ($(".product-image-slider").length) {
            $('.product-image-slider .slick-active img').elevateZoom({
                zoomType: "inner",
                cursor: "crosshair",
                zoomWindowFadeIn: 500,
                zoomWindowFadeOut: 750
            });
        }
        //Filter color/Size
        $('.list-filter').each(function () {
            $(this).find('a').on('click', function (event) {
                event.preventDefault();
                $(this).parent().siblings().removeClass('active');
                $(this).parent().toggleClass('active');
                $(this).parents('.attr-detail').find('.current-size').text($(this).text());
                $(this).parents('.attr-detail').find('.current-color').text($(this).attr('data-color'));
            });
        });
        //Qty Up-Down
        $('.detail-qty').each(function () {
            var qtyval = parseInt($(this).find('.qty-val').text(), 10);

            var qtyInput = document.getElementById("qty-input")
            if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

            $('.qty-up').on('click', function (event) {
                event.preventDefault();
                qtyval = qtyval + 1;
                $(this).prev().text(qtyval);
                if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

            });
            $('.qty-down').on('click', function (event) {
                event.preventDefault();
                qtyval = qtyval - 1;
                if (qtyval > 1) {
                    $(this).next().text(qtyval);
                    if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

                } else {
                    qtyval = 1;
                    $(this).next().text(qtyval);
                    if (qtyInput) { document.getElementById("qty-input").value = qtyval; }

                }
            });
        });

        $('.dropdown-menu .cart_list').on('click', function (event) {
            event.stopPropagation();
        });

        productDetails();
    }

});




$(document).ready(function() {
  $('#submitSignUp').click(function () {
    $(this).css('display', 'none')
    $('#buttonload').css('display', 'inline-block')
  })
})

// ----------------------------------------------------------------------------------
