(function($){
    $('document').ready(function(){
	$('.grid-tile').wookmark({
	    container: $('#grid-container'),
	    offset: 10,
	    autoResize: true,
	    align: 'center',
	});
    });

    $(window).load(function(){
	$('#grid-container').trigger('refreshWookmark');
    });

})(jQuery);
