App.Views.RegisterForm = Backbone.View.extend({
    initialize: function(){
	this.$el.submit(this.onSubmit);
    },
    onSubmit: function(event){
	$.post('/api/account/register', this.$el.serialize(), this.onResp, 'json');	
    },
    onResp: function(resp){
	if (resp.login && resp.status) {
	    App.init();
	}
	else {
	    this.onError(resp.error);
	}
    }
    onError: function(error){
	console.log(error);
    }
});
