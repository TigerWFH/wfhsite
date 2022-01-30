// 处理common-banner逻辑

$('#carousel').click(() => {
  console.log('click');
});

$('document').ready(() => {
  $('#stage div').each(function (index) {
    console.log('index===>', index, this);
    let cl = 'first';
    switch (index) {
      case 0:
        break;
      case 1:
        cl = 'second';
        break;
      case 2:
        cl = 'third';
        break;
      case 3:
        cl = 'fourth';
        break;
      case 4:
        cl = 'fifth';
        break;
      case 5:
        cl = 'sixth';
        break;
    }
    $(this).addClass(cl);
  });
});
