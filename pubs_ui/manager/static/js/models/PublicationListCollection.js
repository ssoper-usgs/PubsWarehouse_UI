/* jslint browser: true */

define([
	'backbone',
	'module'
], function(Backbone, module) {
	"use strict";

	var collection = Backbone.Collection.extend({
		url : module.config().scriptRoot + '/manager/services/lists',

		comparator : 'text'
	});

	return collection;
})