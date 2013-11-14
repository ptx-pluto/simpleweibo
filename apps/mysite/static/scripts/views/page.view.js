App.Views.Page = Backbone.View.extend({
    initialize: function(){},

    render: function(){},

    // route: function(route){
    // 	if (route === 'home') {
    // 	    App.models.current_stream = new App.Models.Stream({ name: 'home' });
    // 	    App.views.current_stream = new App.Views.Stream({ collection: App.models.current_stream });
    // 	    this.$el.
    // 	}
    // 	else if (route === 'root') {
    // 	    App.models.current_stream = new App.Models.Stream({ name: 'root' });
    // 	    App.views.current_stream = new App.Views.Stream({ collection: App.models.current_stream });
    // 	}
    // 	else if (route === 'archive') {
    // 	    App.models.current_stream = new App.Models.Stream({ name: 'archive' });
    // 	    App.views.current_stream = new App.Views.Stream({ collection: App.models.current_stream });
    // 	}
    // },

    welcome: function(){
	this.current_page = new App.Views.WelcomePage;
	this.$el.replaceWith(this.current_page.$el);
    }

});
