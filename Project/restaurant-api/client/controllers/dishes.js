var myApp = angular.module('myApp');

myApp.controller('dishescontrollers',['$scope','$http','$location','$routeParams', function($scope,$http,$location,$routeParams){
    $scope.getDishes = function(){
        $http.get('/api/dishes').success(function(response){
            $scope.dishes=response;
        });
    }
}])