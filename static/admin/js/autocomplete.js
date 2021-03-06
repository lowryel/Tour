'use strict';
{
    const $ = django.jQuery;
<<<<<<< HEAD
    const init = function($element, options) {
        const settings = $.extend({
            ajax: {
                data: function(params) {
                    return {
                        term: params.term,
                        page: params.page,
                        app_label: $element.data('app-label'),
                        model_name: $element.data('model-name'),
                        field_name: $element.data('field-name')
                    };
                }
            }
        }, options);
        $element.select2(settings);
    };

    $.fn.djangoAdminSelect2 = function(options) {
        const settings = $.extend({}, options);
        $.each(this, function(i, element) {
            const $element = $(element);
            init($element, settings);
=======

    $.fn.djangoAdminSelect2 = function() {
        $.each(this, function(i, element) {
            $(element).select2({
                ajax: {
                    data: (params) => {
                        return {
                            term: params.term,
                            page: params.page,
                            app_label: element.dataset.appLabel,
                            model_name: element.dataset.modelName,
                            field_name: element.dataset.fieldName
                        };
                    }
                }
            });
>>>>>>> 4d438c5b3d33aee6930a0f8784376614cc42aa13
        });
        return this;
    };

    $(function() {
        // Initialize all autocomplete widgets except the one in the template
        // form used when a new formset is added.
        $('.admin-autocomplete').not('[name*=__prefix__]').djangoAdminSelect2();
    });

    $(document).on('formset:added', (function() {
        return function(event, $newFormset) {
            return $newFormset.find('.admin-autocomplete').djangoAdminSelect2();
        };
    })(this));
}
