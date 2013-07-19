'use strict';

demoApp.controller('UserCtrl', function ($scope, User) {
	$scope.users = User.query();
});

demoApp.controller('LoginCtrl', function ($scope) {
	$scope.credentials = { username: "", password: ""};
	
	$scope.login = function() {
		console.log($scope.credentials.username);
	};
});
