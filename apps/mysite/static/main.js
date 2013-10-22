/**********************************************************************************
 *
 * Simpleweibo front-end client (based on Backbone.js)
 *
 **********************************************************************************/

(function($){

//====================================================
// Models and Views
//====================================================

var FeedModel = Backbone.Model.extend({});

var FeedView = Backbone.View.extend({
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


var StreamModel = Backbone.Collection.extend({
    model: FeedModel,

    initialize: function(models, options){
	this.id = options.id;
	this.uri = '/api/stream/' + this.id;
	this.fetch();
    },

    fetch: function(){
	var self = this;
	$.get(this.uri, function(data){
	    self.add(data);
	});
    }
});


var StreamView = Backbone.View.extend({
    collection: StreamModel,

    initialize: function(){
	this.$el = $('#grid-container');
	this.view_head = 0;
	this.view_tail = 0;
	this.feed_views = [];
	this.render();
	this.listenTo(this.collection, 'add', this.render);
    },

    render: function(){
	var self = this;
	this.collection.rest(this.view_head).forEach(function(model){
	    var new_feed_view = new FeedView({
		model: model
	    });
	    self.feed_views.push(new_feed_view);
	    self.$el.append(new_feed_view.$el);
	});
	this.view_head = this.collection.length;
	$('.grid-tile').wookmark({
	    container: $('#grid-container'),
	    offset: 10,
	    autoResize: true,
	    align: 'center',
	});
//	this.$el.trigger('refreshWookmark');
	return this;
    }
});

var site_state = {
    streams_m: [],
    streams_v: [],
    settings: {},

    add_stream: function(stream_id){
	var s_m = new StreamModel([], { id: stream_id });
	var s_v = new StreamView({
	    collection: s_m
	});
	this.streams_v.push(s_v);
	this.streams_m.push(s_m);
	return s_m;
    }

};

var home_model = site_state.add_stream('home');


//====================================================
// Site Behavior
//====================================================

// var Workspace = Backbone.Router.extend({
//     routes: {
// 	'url1/:param': 'event1',
// 	'url2/:param': 'event2',
// 	'url3/:param': 'event3',
//     },

//     event1: function(param){ console.log(param); },

//     event2: function(param){ console.log(param); }
// });

// var app_router = new Workspace;

// Backbone.history.start();


})(jQuery);
