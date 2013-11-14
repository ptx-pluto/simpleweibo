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

