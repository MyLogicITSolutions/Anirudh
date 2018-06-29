var myApp = angular.module('myApp',['ngRoute']);

myApp.config(function($routeProvider){
    $routeProvider.when('/',{
        controller:'dishescontrollers',
        templateUrl:'views/dishes.html'
    })
    .otherwise({
        redirectTo: '/'
    })
});


myApp.controller('dishescontrollers',['$scope','$http','$location','$routeParams', function($scope,$http,$location,$routeParams){
    $scope.getDishes = function(){
        $http({ method: 'GET', url:'/api/dishes'}).then(function(response){
            
            $scope.dishes=response.data;
        });
    }
}]);