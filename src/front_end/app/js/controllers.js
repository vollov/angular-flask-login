'use strict';

demoApp.controller('UserCtrl', function ($scope, User) {
	$scope.users = User.query();
});

demoApp.controller('LoginCtrl', function ($scope, $location) {
	$scope.credentials = { username: "", password: ""};
	
	$scope.login = function() {
		if($scope.credentials.username === "dustin") {
			$location.path('/home');
		}
		//console.log($scope.credentials.username);
	};
});
