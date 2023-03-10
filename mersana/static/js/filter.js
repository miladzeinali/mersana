$(document).ready(function () {
    $('.ajaxLoader').hide()
    $(".filter-checkbox").on('click', function () {
        let _filterObj = {};
        $(".filter-checkbox").each(function (index, ele) {
            let _filterVal = $(this).val();
            let _filterKey = $(this).data('filter');
            // [document.querySelectorAll('input[data-filter='+_filterKey+']:checked')].map(function(el){
            //     return el.value;
            // });
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked'))
                .map(function (el) {
                    return el.value;

                });
        });
        //  Run Ajax
        console.log(_filterObj)
        $.ajax({
            url: '/shop/filter-data',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function () {
                $('.ajaxLoader').show()
            },
            success: function (res) {
                console.log(res)
                $('#filterProducts').html(res.data)
                $('.ajaxLoader').hide()
            }

        })
    })
})