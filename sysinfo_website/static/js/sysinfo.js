var app = angular.module('sysinfoApp',['angular-sysinfo']);

app.controller('sysinfoCtrl',function($scope,$log,streamStatus,smartlockService,Constants){
    $scope.constants = Constants;
    $scope.lockstatus = streamStatus;
    smartlockService.getAccount()
    .then(
        function(retvalue){
            $scope.lockstatus.collection = retvalue.results;
            app.globcoll = retvalue.results;
        },
        function(error){
            $log.error(error);
        }
    );
    
});

angular.module('ui.bootstrap.demo', ['ngAnimate', 'ngSanitize', 'ui.bootstrap']);
angular.module('ui.bootstrap.demo').controller('TabsDemoCtrl', function ($scope, $window) {
  $scope.tabs = [
    { title:'Dynamic Title 1', content:'Dynamic content 1' },
    { title:'Dynamic Title 2', content:'Dynamic content 2', disabled: true }
  ];

  $scope.alertMe = function() {
    setTimeout(function() {
      $window.alert('You\'ve selected the alert tab!');
    });
  };

  $scope.model = {
    name: 'Tabs'
  };
});