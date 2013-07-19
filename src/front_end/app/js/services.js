'use strict';

demoApp.factory('User', function($resource) {
	return $resource('/api/users/:id', {id: '@id'}, {
        update: {method:'PUT'}
    });
});
