var Collapse = (function () {
    'use strict';

    ready(init);

    function init() {
        var i;
        var qs = document.querySelectorAll('.collapsable');
        if (qs.length > 0) {
            for (i = 0; i < qs.length; ++i) {
                init_fieldset(qs[i]);
            }
        }
    };

    function init_fieldset(fs) {
        fs._t = fs.querySelector('h2');
        if (fs._t) {
            fs._t._fs = fs;
            fs._t.addEventListener('click', toggle_fieldset);
        }
    };

    function toggle_fieldset(e) {
        var fs = this._fs;
        if (fs) {
            fs.classList.toggle('closed');
        }
    }

    function ready(callback) {
        if (document.readyState != 'loading') {
            callback();
        } else {
            document.addEventListener('DOMContentLoaded', callback);
        }
    };
})();