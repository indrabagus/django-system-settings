var app = angular.module('lockstatusApp',['angular-websocket']);
app.globcoll;
app.constant('Constants',{
    LockStatus:{
        0:'Checked In',
        1:'Checked Out'
    }
});
app.service("smartlockService", function ($http, $q,Constants) {
       var deferred = $q.defer();
       this.getAccount = function () {
           return $http.get('/smartlock/api/v1/smartlockview.json',{
                                params:{'ob':1}
                })
                .then(function (response) {
                    console.log(response.data)
                   // promise is fulfilled
                   deferred.resolve(response.data);
                   // promise is returned
                   return deferred.promise;               
                   
               }, function (response) {
                   // the following line rejects the promise 
                   deferred.reject(response);
                   // promise is returned
                   return deferred.promise;               
                   
               });
       };
   });
   


app.factory('streamStatus',function($websocket,$log,smartlockService){
    var collection;
    var errmsg;
    var datastream;
    
    var startstreaming = function(host){
        // for unsecure websocket, use 'ws://'
        datastream=$websocket('wss://'+host+'/smartlock/accesslog/stream/');
        datastream.onMessage(function(message){
            $log.log('onMessage: ',message.data);
            var res;
            try{
                res = JSON.parse(message.data);
            } catch(e){
                res = {
                    'log_id'    : -1, 
                    'identifier': -1, 
                    'term_id'   : -1,
                    'checked_tm': null,
                    'lockstatus': 0,
                    'info'      : event.data
                };
            }
            // remove end of array element
            if(app.globcoll.length > 100){
                app.globcoll.splice(-1,1);
            }
            //insert to the front of array
            app.globcoll.unshift({
                log_id          : res.id,
                scard_id_str    : res.identifier,
                term_id         : res.term_id,
                checked_tm      : res.checked_tm,
                lockstatus      : res.lockstatus,
                info            : res.info
            });
        });        
    }
    return {
        collection      : app.globcoll,
        startstreaming  : startstreaming
    };
});



app.controller('lockstatusCtrl',function($scope,$log,streamStatus,smartlockService,Constants){
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