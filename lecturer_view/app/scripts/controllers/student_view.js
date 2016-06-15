app.controller('StudentViewCtrl', function($scope, $window, $location, $http){
  if (!$window.localStorage.token) {
    $location.path('/');
    return;
  }
  $scope.left_hover = false; 
  $scope.right_hover = false;
  $scope.current = false;
  $scope.toggle_follow = true;

  $scope.backhome = function(){
    $location.path('/mainmenu');
  }
  var ctrl = $scope;

  $scope.ques = [];

  $scope.question = ""
  
  $scope.addQuestion = function() {
    $http.post(url.concat('/slides/lecture/question/'), $scope.question).success(function(data){
      $scope.update_question();
    });
    $scope.question = '';
  };

  $scope.upvote = function(pk) {
    $http.get(url.concat('/slides/lecture/qvote/')+pk).success(function(data){
      $scope.update_question();
    });
  };
  $scope.update_question = function(){
    console.log('update q called')
    $http.get(url.concat('/slides/lecture/get_page_questions/')).success(function(data){
       $scope.ques = eval(data)
    });
  };
  $scope.happy = function(){
    return $http.get(url.concat('/slides/lecture/vote_up/'));
  };
  $scope.unhappy = function(){
    return $http.get(url.concat('/slides/lecture/vote_down/'));
  };
  $scope.get_mood = function(){
    return $http.get(url.concat('/slides/lecture/get_mood/'));
  };
  $scope.prev = function(){
    return $http.get(url.concat('/slides/lecture/go_prev_page/'));
  };
  $scope.next = function(){
    return $http.get(url.concat('/slides/lecture/go_next_page/'));
  };
  $scope.follow = function(){
      return $http.get(url.concat('/slides/lecture/go_curr_page/'));
  };
  $scope.fast = false;
  $scope.slow = false;
});
