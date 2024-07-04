$(document).ready(function() {
    // Función para editar un producto
    $('.edit-btn').click(function() {
        var productId = $(this).data('id');
        $.ajax({
            url: 'http://127.0.0.1:8000/api/items/' + productId + '/',
            type: 'GET',
            success: function(data) {
                $('#product-id').val(data.id);
                $('#product-nombre').val(data.nombre);
                $('#product-descripcion').val(data.descripcion);
                $('#product-precio').val(data.precio);
            },
        });
    });

    // Botón de eliminar clic
    $('.delete-btn').on('click', function() {
        var productId = $(this).data('id');
        var pathUrl = 'http://127.0.0.1:8000/api/items/' + productId + '/'; // URL de la solicitud DELETE

        if (confirm('¿Estás seguro de que quieres eliminar este producto?')) {
            $.ajax({
                url: pathUrl,
                type: 'DELETE',
                success: function(result) {
                    // Eliminar la fila de la tabla
                    $('tr').filter("[data-id='" + productId + "']").remove();
                },
                error: function(xhr, status, error) {
                    console.log('Hubo un error al eliminar el producto');
                }
            });
        }
    });

    // Función para crear/actualizar un producto
    $('#product-form').submit(function(e) {
        e.preventDefault();
        var productId = $('#product-id').val();
        var url = 'http://127.0.0.1:8000/api/items/' + (productId ? productId + '/' : '');
        var method = productId ? 'PUT' : 'POST';

        var formData = new FormData(this);
        $.ajax({
            url: url,
            type: method,
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                location.reload();
            },
        });
    });
});
