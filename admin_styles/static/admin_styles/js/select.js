var SelectNice = (function () {
    'use strict'

    ready(init);

    function init() {
        var qs = document.querySelectorAll('select.select-nice');
        if (qs) {
            for (var i = 0; i < qs.length; ++i) {
                new SlimSelect({ select: '#' + qs[i].id });
            }
        }
    };

    function ready(callback) {
        if (document.readyState != 'loading') {
            callback();
        } else {
            document.addEventListener('DOMContentLoaded', callback);
        }
    };
})();