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


    });

    $(window).load(function(){
	$('#grid-container').trigger('refreshWookmark');
    });

})(jQuery);
