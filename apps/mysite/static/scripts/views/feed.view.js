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
