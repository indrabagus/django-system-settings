var app = angular.module('sysinfoApp', ['ngAnimate', 'ngSanitize', 'ui.bootstrap']);
app.controller('linuxsysinfoCtrl', function ($scope,$http) {
  $scope.model = {
    "System": "xLinux",
    "Linux Distribution" :"LinuxMint - 18.2 - sonya",
    "Architecture":"64bit ELF"    
  };
  $http.get('/api/v1/linuxsysinfo.json',{
    params:{}
  }).then(function (response) {
    console.log(response.data)
    $scope.linuxsysinfo = response.data    
  },function (error) {
    console.log(error.data)
  });

});