// Add to cart
$(document).on('click','#addtocart', function(){
   let qty = $('#qty').val() ; 
   let code = $('#product-code').val()
   //ajax
   $.ajax({
    url: '/cart/addtocart',
    data: {
        'code': code,
        'qty':qty
    },
    dataType: 'json',
    // beforeSend: function () {
    //     $('.ajaxLoader').show()
    // },
    success: function (res) {
        console.log(res)
       
    }

})
})