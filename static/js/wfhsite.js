$(document).ready(function () {
  // 处理banner
  function initBanner() {
    const bannerWidth = $('#common_banner').width();
    const bannerHeight = $('#common_banner').height();
    const total = $('#common_banner ul li').length;
    const totalWidth = bannerWidth * (total + 1);
    const GAP = 2000;

    $('#banner_dot span:first-child').addClass('active');
    $('#common_banner ul').css('width', totalWidth);
    $('#common_banner ul li:last-child').after(
      $('#common_banner ul li:first-child').clone()
    );
    $('#common_banner ul li').each(function (index) {
      $(this).css({
        width: bannerWidth,
        height: bannerHeight
      });
    });

    let count = 0;
    let begin = Date.now();
    const gap = 3000; // 动画间隔
    function move() {
      const timer = window.requestAnimationFrame(move);
      const end = Date.now();
      if (end - begin >= gap) {
        begin = Date.now();
        count++;
        let offset = count * bannerWidth;
        $('#common_banner ul').stop();
        if (count === total) {
          count = 0;
          $('#banner_dot span').each(function (index) {
            if (count === index) {
              $(this).addClass('active');
            } else {
              $(this).removeClass('active');
            }
          });
          $('#common_banner ul').animate(
            {
              left: -offset
            },
            500,
            function () {
              $('#common_banner ul').css({
                left: 0
              });
            }
          );
        } else {
          $('#common_banner ul').animate(
            {
              left: -offset
            },
            500
          );
          $('#banner_dot span').each(function (index) {
            if (count === index) {
              $(this).addClass('active');
            } else {
              $(this).removeClass('active');
            }
          });
        }
      }
    }

    move();
  }

  initBanner();
});
