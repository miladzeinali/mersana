jQuery(function($) {'use strict';

	// Navigation Scroll
	// $(window).scroll(function(event) {
	// 	Scroll();
	// });

	$('.navbar-collapse ul li a').on('click', function() {  
		$('html, body').animate({scrollTop: $(this.hash).offset().top - 5}, 1000);
		return false;
	});



	$('#tohash').on('click', function(){
		$('html, body').animate({scrollTop: $(this.hash).offset().top - 5}, 1000);
		return false;
	});


	
	

	//Initiat WOW JS
	new WOW().init();
	//smoothScroll
	// smoothScroll.init();



	$(document).ready(function() {
		//Animated Progress
		$('.progress-bar').bind('inview', function(event, visible, visiblePartX, visiblePartY) {
			if (visible) {
				$(this).css('width', $(this).data('width') + '%');
				$(this).unbind('inview');
			}
		});

		// Animated Number
		$.fn.animateNumbers = function(stop, commas, duration, ease) {
			return this.each(function() {
				var $this = $(this);
				var start = parseInt($this.text().replace(/,/g, ""));
				commas = (commas === undefined) ? true : commas;
				$({value: start}).animate({value: stop}, {
					duration: duration == undefined ? 1000 : duration,
					easing: ease == undefined ? "swing" : ease,
					step: function() {
						$this.text(Math.floor(this.value));
						if (commas) { $this.text($this.text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,")); }
					},
					complete: function() {
						if (parseInt($this.text()) !== stop) {
							$this.text(stop);
							if (commas) { $this.text($this.text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,")); }
						}
					}
				});
			});
		};

		$('.animated-number').bind('inview', function(event, visible, visiblePartX, visiblePartY) {
			var $this = $(this);
			if (visible) {
				$this.animateNumbers($this.data('digit'), false, $this.data('duration')); 
				$this.unbind('inview');
			}
		});
	});

	$(document).ready(function() {
		var contentWayPoint = function() {
			var i = 0;
			$('.ftco-animate').waypoint( function( direction ) {
	
				if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {
					
					i++;
	
					$(this.element).addClass('item-animate');
					setTimeout(function(){
	
						$('body .ftco-animate.item-animate').each(function(k){
							var el = $(this);
							setTimeout( function () {
								var effect = el.data('animate-effect');
								if ( effect === 'fadeIn') {
									el.addClass('fadeIn ftco-animated');
								} else if ( effect === 'fadeInLeft') {
									el.addClass('fadeInLeft ftco-animated');
								} else if ( effect === 'fadeInRight') {
									el.addClass('fadeInRight ftco-animated');
								} else {
									el.addClass('fadeInUp ftco-animated');
								}
								el.removeClass('item-animate');
							},  k * 50, 'easeInOutExpo' );
						});
						
					}, 100);
					
				}
	
			} , { offset: '95%' } );
		};
		contentWayPoint();
	})

	

});