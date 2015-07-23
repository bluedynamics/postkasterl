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
            var target_url = form_element.attr('action');
            form_element.submit(function( event ) {
                event.preventDefault();
                var form_data = form_element.serializeArray();
                $.post(
                    target_url,
                    form_data,
                    function(){},
                    'json'
                ).success(function(data) {
                    alert('cool: ');
                }).fail(function() {
                    alert('not so cool');
                });
            });
        }
    });

})(jQuery);
