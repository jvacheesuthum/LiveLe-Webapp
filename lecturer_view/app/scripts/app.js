var app = angular.module('frontendApp',[
    'ngCookies',
    'ngResource',
    'ngSanitize',
    'ngRoute'
]);

app.config(['$routeProvider','$httpProvider', function($routeProvider, $httpProvider) {
  $httpProvider.interceptors.push('AuthInterceptor');
  $routeProvider
    .when('/', {
      templateUrl: 'views/auth.html',
      controller: 'AuthCtrl'
    })
    .when('/mainmenu', {
      templateUrl: 'views/mainmenu.html',
      controller: 'MainmenuCtrl'

    })
    .when('/lecture', {
      templateUrl: 'views/lecture.html',
      controller: 'LectureCtrl'
    })
    .when('/questions', {
      templateUrl: 'views/questions.html',
      controller: 'questionCtrl'
    })
    .when('/clicker_login', {
      templateUrl: 'views/clicker_login.html',
      controller: 'ClickerLoginCtrl'
    })
    .when('/clicker', {
      templateUrl: 'views/clicker.html',
      controller: 'ClickerCtrl'
    })
    .when('/student_view', {
      templateUrl: 'views/student_view.html',
      controller: 'StudentViewCtrl'
    })
    .when('/student_mainmenu', {
      templateUrl: 'views/student_mainmenu.html',
      controller: 'StudentMainmenuCtrl'
    })
    .otherwise({
      redirectTo: '/'
    });
}]);

var url = 'http://146.169.47.210:8000';
//app.constant('API_SERVER', 'http://127.0.0.1:8000/slides/api/');
app.constant('API_SERVER', url.concat('/slides/api/'));
