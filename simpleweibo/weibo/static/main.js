(function($){
    $('document').ready(function(){
	$('.grid-tile').wookmark({
	    container: $('#grid-container'),
	    offset: 10,
	    autoResize: true,
	    align: 'center',
	});

	$('form').each(function(){
	    $('input').keypress(function(e){
		if (e.which == 10 || e.which == 13) {
		    this.form.submit();
		}
	    });
	});

	$('.profile-front').bind('click', function(){
	    var elem = $(this)

	    if (elem.data('flipped')){
		elem.revertFlip();
		elem.data('flipped', false)
	    }
	    else {
		elem.flip({
		    direction: 'lr',
		    speed: 350,
		    onBefore: function(){
			elem.html(elem.siblings('.profile-back').html());
		    }
		});
		elem.data('flipped', true);
	    }
	    
	});

    });

    $(window).load(function(){
	$('#grid-container').trigger('refreshWookmark');
    });

})(jQuery);
