App.Models.Account = Backbone.Model.extend({
    defaults: {
	'login': false
    },

    initialize: function(){
	this.fetch();
    },

    fetch: function(){	
	var self = this;
	$.get('/api/account', function(data){
	    if (data.login) {
		self.login = true;
		App.init();
	    }
	    else {
		App.auth();
	    }
	    
	});
    },

    login: function(){},

    register: function(){}

});
