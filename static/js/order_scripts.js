window.onload = function () {
    var _qantity, _price, delta_quantity, orderitem_quantity, delta_cost;
    var quantity_arr = [];
    var price;

    var TOTAL_FORMS = parseint($('input[name="orderitems=TOTAL_forms"]').val());

    var order_total_quantity = parseint($('.order_total_quantity').text()) || 0;
    var order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for (var i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantity_arr[i] = _quantity;
        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }
}