'use strict';

module.exports = function(grunt) {

    grunt.initConfig({

	pathConfig: {
	    app: 'app',
	    dist: '.tmp/dist',
	    build: '.tmp/build',
	    release: 'dist'
	},

	venders: 'app/venders',

	pkg: grunt.file.readJSON('package.json'),

	concat: {
	    build: {
		files: {
		    '.tmp/build/application.js': 'app/scripts/*.js', 
		    '.tmp/build/libs.js': [
			'<%= venders %>/jquery/jquery.js',
			'<%= venders %>/handlebars/handlebars.js',
			'<%= venders %>/ember/ember.js'
//			'<%= venders %>/ember-data/ember-data.js'
		    ]
		}
	    }
	},

	uglify: {
	    dist: {
		files: {
		    '.tmp/dist/main.js': [
			'<%= pathConfig.build %>/application.js',
			'<%= pathConfig.build %>/libs.js'
		    ]
		}
	    }
	},

	emberTemplates: {
	    options: {
		templateName: function(tName) {
		    return tName.replace('app/templates/', '');
		}
	    },

	    build: {
		files: {
		    '.tmp/build/templates.js': 'app/templates/*.hbs'
		}
	    }

	},

	copy: {
	    build: {
		files: {
		    '.tmp/build/index.html': 'app/index.html'
		}
	    }
	},

	watch: {}

    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-ember-templates');

    grunt.registerTask('build', ['concat:build', 'emberTemplates:build', 'copy:build']);
    grunt.registerTask('dist', ['build', 'uglify:dist']);

};
