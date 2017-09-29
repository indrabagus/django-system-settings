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