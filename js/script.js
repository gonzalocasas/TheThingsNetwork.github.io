console.log("hello");

$(function(fade) {
$(".welcome").hide(0).delay(0).fadeIn(1500);
});

$(function(jump) {
$(".logo-img").hide(0).delay(0).fadeIn(2000);
});

$(function(particles){
$(".animation").jParticle({
        
    // number of particles
    particlesNumber: 100,


// Distance where link is full opacity
    linkDist: 50,

// Distance where particles start linking.
    createLinkDist: 120,

// disable links between particles
    disableLinks: false,

// disable mouse interaction
    disableMouse: false,

// background color
    background: 'transparent',

// Particles and links color.
    color: 'white',

// container's width/height
    width: 1280,
    height: 637,

// Links width in pixels
    linksWidth: 1,

    particle: {

  // Particles color.
        color: "white",

  // min / max size
        minSize: 2,
        maxSize: 8,

  // animation speed
        speed: 30
    }
});
});

$(function(stickUp) {
$(".nav").stickUp();

});








