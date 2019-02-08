(function($) {
	
	"use strict";
    
		/* Closes the Responsive Menu on Menu Item Click*/
		$('.navbar-collapse ul li a').on('click', function() {
			$('.navbar-toggle:visible').click();
		});
		/*END MENU JS*/ 
    /* ----------------------------------------------------------- */
	/*  Fixed header
	/* ----------------------------------------------------------- */
    
     
    $(window).on('scroll', function(){
		if ( $(window).scrollTop() > 70 ) {
			$('.site-navigation,.center-navigation').addClass('header-white');
		} else {
			$('.site-navigation,.center-navigation').removeClass('header-white');
		}
        
        
        $('.slick-slider-banner').slick({
          dots: false,
          autoplay: true,
          infinite: true,
          mobileFirst: true,
          autoplaySpeed: 3000,
          slidesToShow: 1,
          centerMode: true,
          variableWidth: true,
            responsive: [
                {
                  breakpoint: 1024,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                  }
                },
                {
                  breakpoint: 600,
                  settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                  }
                },
                {
                  breakpoint: 480,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                }
              ]
        });
	});
    
    
    /*================================
    stickey Header
    ==================================*/
    
    
      jQuery(document).on('ready', function(){   
          
	/* ----------------------------------------------------------- */
	/*  Mobile Menu
	/* ----------------------------------------------------------- */

	jQuery(".nav.navbar-nav li a").on("click", function() { 
		jQuery(this).parent("li").find(".dropdown-menu").slideToggle();
		jQuery(this).find("i").toggleClass("fa-angle-down fa-angle-up");
	});
          
          
	});

		
/* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */
      if ($(".slider").length)
      {
  $(".slider").owlCarousel({
         items: 1,
         loop: true,
         autoplay: false,
         nav: false,
         dots: true,
         autoplayTimeout: 5000
      });
            
      }
  
		
})(window.jQuery);