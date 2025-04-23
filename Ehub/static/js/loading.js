window.onload = function() {
  setTimeout(function() {
    window.location.href = "{% url 'home' %}";  
  }, 3500);  
};