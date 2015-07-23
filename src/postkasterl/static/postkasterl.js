/*
 * postkasterl javascript
 * requires jQuery
 *
 */

if (typeof(window.postkasterl) == "undefined") postkasterl = {};

(function($) {

    $.extend(postkasterl, {

        bind: function(selector) {
            var form_element = $(selector);
            console.log('bind postkasterl ' + selector);
        }
    });

})(jQuery);
