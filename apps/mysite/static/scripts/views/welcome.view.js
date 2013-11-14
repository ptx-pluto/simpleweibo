define(['jquery','backbone'], function ($, Backbone) {
//App.Views.WelcomePage = Backbone.View.extend({
    var WelcomePage = Backbone.View.extend({
	$el: $.parseHTML($('#welcome-page').html()),
	initialize: function(){
	    this.login_form = new App.Views.LoginForm({ $el: $('#login-form', this.$el) });
	    this.register_form = new App.Views.RegisterForm({ $el: $('#register-form', this.$el) });
	}
    });
    return WelcomePage;
});
