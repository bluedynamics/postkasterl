/*
 * postkasterl javascript
 * requires jQuery
 *
 */

if (typeof(window.postkasterl) == "undefined") postkasterl = {};

(function($) {

    $.extend(postkasterl, {

        bind: function(selector) {
            var element = $(selector);
            console.log('bind postkasterl ' + selector + element);
        }
    });

})(jQuery);
