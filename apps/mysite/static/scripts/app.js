/**********************************************************************************
 *
 * Simpleweibo front-end client (based on Backbone.js)
 *
 **********************************************************************************/

window.App = {
    Models: {},
    Views: {},
    models: {},
    views: {},
};

App.Workspace = Backbone.Router.extend({

    routes: {
	'stream/root': 'index_page',
	'stream/home': 'home_page',
	'stream/archive': 'archive_page',
//	'stream/profile/:uid': 'stream_page',
	'*default': 'home_page'
    },

    index_page: function(){ 
	console.log('you triggered index page'); 
	App.views.page.route('root');
    },

    home_page: function(){ 
	console.log('you triggered home page'); 
	App.views.page.route('home');
    },

    archive_page: function(){ 
	console.log('you triggered archive page'); 
	App.views.page.route('archive');
    }

});


App.init = function(){
    App.router = new App.Workspace;
    Backbone.history.start();
};


App.auth = function(){
    App.views.page.welcome();
};


// DOM ready
$(function(){
    App.models.account = new App.Models.Account;
    App.views.page = new App.Views.Page({ model: App.model.account });
});

