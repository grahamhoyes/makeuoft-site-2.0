var skipScrollUpdate = false;
var matrixGraphicIndex = 0; // 0: make, 1: uoft
var matrixGraphicInterval;

$(document).ready(function() {

    // Animate the MakeUofT matrix graphic
    matrixGraphicInterval = setInterval(function() {
        if (matrixGraphicIndex == 0) {
            $('#Make-Matrix').attr('opacity', '0');
            $('#UofT-Matrix').attr('opacity', '1');
            matrixGraphicIndex = 1;
        } else {
            $('#UofT-Matrix').attr('opacity', '0');
            $('#Make-Matrix').attr('opacity', '1');
            matrixGraphicIndex = 0;
        }
    }, 3141);

    // Countdown to registration opening
    var makeathonDate = new Date("Dec 16, 2019 09:00:00").getTime();
    setInterval(function() {
        var now = new Date().getTime();
        var remaining = makeathonDate - now;
        var days = Math.floor(remaining / (1000 * 60 * 60 * 24));
        var hours = Math.floor((remaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((remaining % (1000 * 60)) / 1000);
        $('#countdown-days').html(days);
        $('#countdown-hours').html(hours);
        $('#countdown-minutes').html(minutes);
        $('#countdown-seconds').html(seconds);
        $('#countdown').html(days + 'D ' + hours + 'H ' + minutes + 'M ' + seconds + 'S');
    }, 1000);

    $('#about-a').click(function() {
        $('.section-active').removeClass('section-active');
        $('#about-a').addClass('section-active');
        skipScrollUpdate = true;
    });
    $('#faq-a').click(function() {
        $('.section-active').removeClass('section-active');
        $('#faq-a').addClass('section-active');
        skipScrollUpdate = true;
    });
    $('#sponsors-a').click(function() {
        $('.section-active').removeClass('section-active');
        $('#sponsors-a').addClass('section-active');
        skipScrollUpdate = true;
    });
    $('#contact-a').click(function() {
        $('.section-active').removeClass('section-active');
        $('#contact-a').addClass('section-active');
        skipScrollUpdate = true;
    });
    /*$('#schedule-a').click(function() {
        $('.section-active').removeClass('section-active');
        $('#schedule-a').addClass('section-active');
        skipScrollUpdate = true;
   });*/
    $('#top-bar li').click(function() {
        $('.title-bar').foundation('toggleMenu');
    });

    $(document).scroll(function() {
        if($(window).scrollTop() > 50) {
            $(".top-bar").addClass("top-bar-active");
        } else {
            //remove the background property so it comes transparent again (defined in your css)
           $(".top-bar").removeClass("top-bar-active");
        }
        if (skipScrollUpdate) {
            skipScrollUpdate = false;
            return;
        }
        $('.section-active').removeClass('section-active');

        // Need to compute these every time in case an FAQ was expanded
        var landingTop = $('#section-landing').offset().top; // Also the height of the header
        //var scheduleTop = $('#section-schedule').offset().top;
        var aboutTop = $('#section-about').offset().top;
        var faqTop = $('#section-faq').offset().top;
        //var sponsorsTop = $('#section-sponsors').offset().top;
        var footerTop = $('#footer').offset().top;

        var positionTop = $(document).scrollTop();
        var activePosition = positionTop + $(window).height()*(2/3); // Don't update the live colours until it's 1/3 of the way on the page


/*        if (activePosition > footerTop) {
            $('#contact-a').addClass('section-active');
        } else if (activePosition > sponsorsTop) {
            //$('#sponsors-a').addClass('section-active');
        } else if (activePosition > faqTop) {
            $('#faq-a').addClass('section-active');
        } else if (activePosition > aboutTop) {
            $('#about-a').addClass('section-active');
        } else if (activePosition > scheduleTop) {
            $('#schedule-a').addClass('section-active');
        }*/
    });

    // Reset application modal when opened
    $('#apply-a').click(function() {
        $('#registration-email-error').html('');
        $('#registration-password-error').html('');
        $('#registration-confirm-password-error').html('');
        $('#registration-success').html('');
        $('#user-registration').find('input[name="email"]').val('')
        $('#user-registration').find('input[name="password"]').val('')
        $('#user-registration').find('input[name="confirm_password"]').val('')
        $('#user-registration').css('display', '')
    })

    // Registration form handling
    $('#user-registration-submit').click(function() {
        var firstname = $('#user-registration').find('input[name="firstname"]').val();
        var lastname = $('#user-registration').find('input[name="lastname"]').val();
        var email = $('#user-registration').find('input[name="email"]').val();
        var password = $('#user-registration').find('input[name="password"]').val();
        var confirm_password = $('#user-registration').find('input[name="confirm_password"]').val();
        var data = {'email': email, 'firstname': firstname, 'lastname': lastname, 'password': password, 'confirm_password': confirm_password};

        // Post the data
        $.post('user_signup.php', data, function(res){
            console.log(res);
            var result = JSON.parse(res);

            // Clear existing error fields
            $('#registration-email-error').html('');
            $('#registration-password-error').html('');
            $('#registration-confirm-password-error').html('');
            $('#registration-success').html('');

            if (result['success'] == true) {
                $('#registration-success').html('Registration successful! Please check your email to activate your account.');
                $('#user-registration').css('display', 'none')
            } else {
                if ('email_error' in result['errors']) {
                    $('#registration-email-error').html(result['errors']['email_error']);
                }
                if ('password_error' in result['errors']) {
                    $('#registration-password-error').html(result['errors']['password_error']);
                }
                if ('confirm_password_error' in result['errors']) {
                    $('#registration-confirm-password-error').html(result['errors']['confirm_password_error']);
                }
                if ('firstname_error' in result['errors']) {
                    $('#registration-firstname-error').html(result['errors']['firstname_error']);
                }
                if ('lastname_error' in result['errors']) {
                    $('#registration-lastname-error').html(result['errors']['lastname_error']);
                }
            }
        });
    });

    // Login handling
    if (window.location.hash.split('#')[1] == 'login') {
        $('#loginModal').foundation('open');
    } else if (window.location.hash.split('#')[1] == 'apply') {
        $('#applyModal').foundation('open');
    }

    //Convienent stuff with location hash
    $('[data-reveal]').on('closed.zf.reveal', () => {
        window.location.hash = '';
    })
	
	

	
	// Form submission
    $('.mailing-list').submit(function(e) {
        e.preventDefault();
		var form = $(this);
		var email = form.find('input[name="email"]').val()
        var data = {'email': email}
        $.post('mailinglist', data, function(result) {
            console.log(result);
            try {
                if (result['success']) {
                    alert(result['message']);
                } else {
                    alert(result['error']);
                }
            } catch (e) {
                alert('Error: ' + e.message);
            }
        });
    });
});

$(document).on('formvalid.zf.abide', function(ev, frm) {
    // Application form is validated by abide. When that happens, we can submit.
    $('#submit-message').html('Submitting, please wait...');
    submit();
});
