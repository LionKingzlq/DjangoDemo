/**
 * Created by abraham on 2016/11/10.
 */
var scotchApp = angular.module('scotchApp');

scotchApp.controller('mainController', function ($scope) {
    $scope.message = 'Everyone come and see how good I look!';
});

scotchApp.controller('aboutController', function ($scope) {
    $scope.message = 'Look! I am an about page.';
});

scotchApp.controller('contactController', function ($scope) {
    $scope.message = 'Contact us! JK. This is just a demo.';
});