app.controller('MainmenuCtrl', function($scope, $http, $window, $location, AuthService){
  if (!$window.localStorage.token) {
    $location.path('/');
    return;
  }
  if ($window.localStorage.user_is_lec != 1) {
    $location.path('/');
    return;
  }
  $scope.token = $window.localStorage.token;
  $scope.username = $window.localStorage.username;
  $scope.logout = function () {
    AuthService.logout().then(
      function () {
        $location.path('/');
      },
      function (error) {
        $scope.error = error;
      }
    );
  };
  $scope.json = {'x': 'nothing'};
  $scope.lecture_list = [];
  $scope.icon_hover = false;

  var ctrl = $scope;

  $scope.getjson = function(){
    $http.get(url.concat('/slides/returnsomejson/')).success(function(data){
      ctrl.json = data;
    });
  };
  $scope.getleclist = function(name){
    $http.get(url.concat('/slides/lecture_list/')+course).success(function(data){
     ctrl.lecture_list = eval(data);
    });
   };
  $scope.select_slide = function(pk){
    $http.get(url.concat('/slides/select_lecture/')+pk).success(function(data){
      // this will jump to another html section with another controller so it will not know about this pk
      $location.path('/lecture');
    });
    console.log('slide selected');
  }

  $scope.course_list = []
  $scope.getcourses = function(){
    $http.get(url.concat('/slides/course_list/')).success(function(data){
     ctrl.course_list = eval(data);
    });
  }
  $scope.select_course = function(course){
    $http.get(url.concat('/slides/lecture_list/')+course).success(function(data){
     ctrl.lecture_list = eval(data);
    });
  }

});

