'use strict';

var demoApp = angular.module('appModule', [ 'ngResource' ]);

demoApp.config(function($routeProvider) {
	$routeProvider.when('/home', {
		templateUrl : 'views/public/home.html'
	}).when('/about', {
		templateUrl : 'views/public/about.html'
	}).when('/users', {
		controller : 'UserCtrl',
		templateUrl : 'views/user/list.html'
	}).otherwise({
		redirectTo : '/home'
	});
});
