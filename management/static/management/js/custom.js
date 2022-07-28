$(document).ready(function () {
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
  var ctx = $("#chart-line");
  var myLineChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      datasets: [
        {
          data: [0, 10, 20, 14, 30, 50, 18, 60, 3, 10, 7, 12],
          label: "Sales",
          borderColor: "rgb(44, 85, 149)",
          fill: true,
          backgroundColor: "rgb(44, 85, 149)",
        },
        {
          data: [12, 7, 10, 2, 10, 12, 14, 4, 20, 50, 40, 30],
          label: "Revenue",
          borderColor: "rgb(238 238 238)",
          fill: false,
          backgroundColor: "rgb(238 238 238)",
        },
      ],
    },
    options: {
      title: {
        display: false,
        //text: "Sales / Revenue",
      },
    },
  });
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
});
