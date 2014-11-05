$(document).ready(function() {

  /* Nav */
  var previousScroll = 0,
  headerHeight = $('header:not(.active)').outerHeight();
  function nav() {
    var currentScroll = $(this).scrollTop();
    if (currentScroll > headerHeight*2) {
      var position = parseInt($('header').css('top').replace(/[^-\d\.]/g, ''));
      if (currentScroll > previousScroll) {
        if(position >= -headerHeight) {
          $('header:not(.active)').css('top', (position-3) + 'px');
        }
      } else {
        if(position <= -3) {
          $('header:not(.active)').css('top', (position+3) + 'px');
        }
      }
    } 
    previousScroll = currentScroll;
    if(!$(window).scrollTop()) {
      $('header:not(.active)').css('top', '0');
    }
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
      $('header:not(.active)').stop().animate({top: 0}, 250);
    }
  }
  $('header span').click(function() {
    if($(this).parent().hasClass('active')) {
      $(this).parent().removeClass('active');
      $('header nav').fadeOut(150);
      $('nav a').removeClass('hidden');
    } else {
      $(this).parent().addClass('active');
      $('header nav').fadeIn(150);
      $('nav a').addClass('hidden');
      setTimeout(function(){
        $('nav a:nth-of-type(1)').addClass('animated fadeInDown');
      }, 200);
      setTimeout(function(){
        $('nav a:nth-of-type(2)').addClass('animated fadeInDown');
      }, 300);
      setTimeout(function(){
        $('nav a:nth-of-type(3)').addClass('animated fadeInDown');
      }, 400);
      setTimeout(function(){
        $('nav a:nth-of-type(4)').addClass('animated fadeInDown');
      }, 500);
    }
  });
  
  /* Process */
  function process() {
    $('body#services section:nth-of-type(3) main ul:first-of-type li').each(function() {
      var width = $(this).css('width');
      $(this).css({'height': width, 'lineHeight' : width});
    });
  }
  process();
  
  /* Work */
  function work() {
    $('body#work section:nth-of-type(2) div, body#work.project section:last-of-type div').each(function() {
      var width = $(this).width();
      $(this).css({'height': width});
    });
  }
  work();
  
  /* Page Animations */
  if (document.documentElement.clientWidth > 1024) {
    $('body#home main h1').addClass('hidden').on("inview",function() {
      $(this).addClass('animated fadeIn');
    });
    $('body#home main h3').addClass('hidden').on("inview",function() {
      setTimeout(function(){
        $('body#home main h3').addClass('animated fadeIn');
      }, 300);
    });
    $('body#home main > a').addClass('hidden').on("inview",function() {
      setTimeout(function(){
        $('body#home main > a').addClass('animated fadeInUp');
      }, 800);
    });
    $('body:not(#home) main > h3').addClass('hidden').on("inview",function() {
      $(this).addClass('animated fadeIn');
    });
    $('body#about section:nth-of-type(1) main div').addClass('hidden').on("inview",function() {
      $(this).addClass('animated fadeIn');
    });
    $('body#about section:nth-of-type(2) img, body#about section:nth-of-type(4) img').each(function() {
      $(this).addClass('hidden').on("inview",function() {
        $(this).addClass('animated fadeIn');
      });
    });
    $('body#services section:nth-of-type(1) main div').addClass('hidden').on("inview",function() {
      $(this).addClass('animated fadeIn');
    });
    $('body#services section:nth-of-type(2) img').each(function() {
      $(this).addClass('hidden').on("inview",function() {
        $(this).addClass('animated fadeIn');
      });
    });
    $('body#services section:nth-of-type(3) main ul li').addClass('hidden')
    $('body#services section:nth-of-type(3) main ul:nth-of-type(2)').on("inview",function() {
      $('body#services section:nth-of-type(3) main ul:first-of-type li:nth-of-type(1)').addClass('animated rollIn');
      setTimeout(function(){
        $('body#services section:nth-of-type(3) main ul:first-of-type li:nth-of-type(2)').delay(50).addClass('animated rollIn');
      }, 100);
      setTimeout(function(){
        $('body#services section:nth-of-type(3) main ul:first-of-type li:nth-of-type(3)').delay(100).addClass('animated rollIn');
      }, 200);
      setTimeout(function(){
        $('body#services section:nth-of-type(3) main ul:first-of-type li:nth-of-type(4)').delay(150).addClass('animated rollIn');
      }, 300);
    });
    $('body#services section:nth-of-type(3) main ul:nth-of-type(2)').on("inview",function() {
      $('body#services section:nth-of-type(3) main ul:last-of-type li:nth-of-type(1)').addClass('animated fadeInLeft');
      setTimeout(function(){
        $('body#services section:nth-of-type(3) main ul:last-of-type li:nth-of-type(2)').delay(50).addClass('animated fadeInLeft');
      }, 100);
      setTimeout(function(){
        $('body#services section:nth-of-type(3) main ul:last-of-type li:nth-of-type(3)').delay(100).addClass('animated fadeInLeft');
      }, 200);
      setTimeout(function(){
        $('body#services section:nth-of-type(3) main ul:last-of-type li:nth-of-type(4)').delay(150).addClass('animated fadeInLeft');
      }, 300);
    });
    $('body#services section:nth-of-type(4) main ul li').each(function() {
      $(this).addClass('hidden').on("inview",function() {
        $(this).addClass('animated fadeIn');
      });
    });
    $('body#work section:nth-of-type(2) div, body#work.project section:last-of-type div').each(function() {
      $(this).addClass('hidden').on("inview",function() {
        $(this).addClass('animated fadeIn');
      });
    });
  }
  
  /* Window Resize Events */
  $(window).resize(function() {
    if (document.documentElement.clientWidth > 767) {
      work();
    }
    process();
    work();
  });
  
  /* Window Scroll Events */
  $(window).scroll(function(){
    if (document.documentElement.clientWidth > 1024) {
      nav();
    }
  });

});
		