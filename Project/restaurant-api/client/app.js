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
