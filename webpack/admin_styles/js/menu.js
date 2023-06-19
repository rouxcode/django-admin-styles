(function () {
    'use strict';

    ready(init);

    function init() {
        var user_menu = document.querySelector('#header .user-menu');
        if (user_menu) {
            var b = user_menu.querySelector('.menu-label');
            if (b) {
                b.addEventListener('click', toggle_menu);
            }
        }

        function toggle_menu(e) {
            e.stopPropagation();
            user_menu.classList.toggle('open');
            document.body.addEventListener('click', hide_menu);
        };

        function hide_menu(e) {
            user_menu.classList.remove('open');
            document.body.removeEventListener('click', hide_menu);
        };
    };

    function ready(callback) {
        if (document.readyState != 'loading') {
            init();
        } else {
            document.addEventListener('DOMContentLoaded', init);
        }
    }
})();