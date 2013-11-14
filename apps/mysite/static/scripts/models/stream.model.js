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
