'use strict';

demoApp.controller('UserCtrl', function ($scope, User) {
	$scope.users = User.query();
});

