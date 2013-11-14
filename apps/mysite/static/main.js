/**********************************************************************************
 *
 * Simpleweibo front-end client (based on Backbone.js)
 *
 **********************************************************************************/

(function($){

window.App = {
    Models: {},
    Views: {},
    models: {},
    views: {},
};


//==============
// Models
//==============

App.Models.Feed = Backbone.Model.extend({});

App.Models.Stream = Backbone.Collection.extend({
    model: FeedModel,
    comparator: 'id',

    initialize: function(models, options){
	this.name = options.name;
	this.uri = '/api/stream/' + this.name;
	this.fetch();
    },

    fetch: function(direction) { 
	var self = this;
	var query = {};

	if (direction === 'old') {
	    var query = { tail: this.at(0)['id'] };
	}
	else if (direction === 'new') {
	    var query = { head: this.last()['id'] };
	}

	$.get(this.uri, query)
	    .done(function(data){
		self.add(data);
	    });
    },

});

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


//========================================================================


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


App.Views.StreamPage = Backbone.View.extend({
    initialize: function(){
	this.$el = $('<div id="stream-page"/>').addClass('row-fluid');
    },
    render: function(){}
});

App.Views.WelcomePage = Backbone.View.extend({
    $el: $.parseHTML($('#welcome-page').html()),
    initialize: function(){
	this.login_form = new App.Views.LoginForm({ $el: $('#login-form', this.$el) });
	this.register_form = new App.Views.RegisterForm({ $el: $('#register-form', this.$el) });
    }
});

App.Views.LoginForm = Backbone.View.extend({
    initialize: function(){
	this.$el.submit(this.onSubmit);
    },
    onSubmit: function(event){
	$.post('/api/account', this.$el.serialize(), this.onResp, 'json');	
    },
    onResp: function(resp){
	if (resp.login && resp.status) {
	    App.init();
	}
	else {
	    this.onError(resp.error);
	}
    },
    onError: function(error){
	console.log(error);
    }
});

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

App.Views.Feed = Backbone.View.extend({
    model: FeedModel,
    template: _.template($('#feed-template').html()),

    initialize: function(){
	this.render();
    },

    render: function(){
	var dom_str = this.template(this.model.attributes);
	this.$el = $.parseHTML(dom_str);
	return this;
    }
});


App.Views.Stream = Backbone.View.extend({
    initialize: function(options){
	this.$el = $.parseHTML($('#stream-container').html());
	$('#main-content').append(this.$el);

	this.view_head = 0;
	this.view_tail = 0;
	this.feed_views = [];

	this.render_all();
	this.listenTo(this.collection, 'add', this.render);

    },

    render_all: function(){
	var self = this;

	this.collection.forEach(function(model){
	    var new_feed_view = new FeedView({ model: model });
	    self.feed_views.push(new_feed_view);
	    self.$el.append(new_feed_view.$el);
	});
	this.view_head = this.collection.at(0)['id']
	this.view_tail = this.collection.at(-1)['id']

	$('.grid-tile', this.$el).wookmark({
	    container: $('.grid-container:first', this.$el),
	    offset: 10,
	    autoResize: true,
	    align: 'center',
	});
    },

    render_new: function(){
	var self = this;
	this.collection
	    .filter(function(model){ return model.id > self.view_head; });
	    .reverse()
	    .forEach(function(model){
		var new_feed_view = new FeedView({ model: model });
		self.feed_views.push(new_feed_view);
		self.$el.prepend(new_feed_view.$el);
	    });
	this.view_head = this.collection.at(0)['id']
	this.view_tail = this.collection.at(-1)['id']
	return this;
    },

    render_old: function(){
	var self = this;
	this.collection
	    .filter(function(model){ return model.id < self.view_tail; })
	    .forEach(function(model){
		var new_feed_view = new FeedView({ model: model });
		self.feed_views.push(new_feed_view);
		self.$el.append(new_feed_view.$el);
	    });    
	this.view_head = this.collection.at(0)['id']
	this.view_tail = this.collection.at(-1)['id']
	return this;
    },
    
    render: function(){
	this.render_new().render_old();
	return this;
    }
});



//===============
// Site Behavior
//===============

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


})(jQuery);
