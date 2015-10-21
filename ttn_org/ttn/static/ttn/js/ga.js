(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-11557232-10', 'auto');
ga('send', 'pageview');


window.track_event = function(category, action, label, value) {
    //console.log("tracking", category, action);
    ga('send', 'event', category, action, label, value);
}

window.open_tracked = function(url, window_name, category, action, label, value) {
    window.track_event(category, action, label, value);
    window.open(url, window_name || '_blank');
}

